import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=330, book=3)

fr_unknown_item = "Vous ne possédez pas cet objet."
fr_has_rope = "Vous possédez une Corde."

fr_text = """
Vous parvenez bientôt au pied d'un escalier en colimaçon ; il
semble qu'il n'y ait pas d'autre choix que de l'emprunter. Après
avoir monté plus de deux cents marches, vous arrivez dans un
couloir qui mène à un balcon. A une dizaine de mètres au-
dessous, vous apercevez Vonotar le Traître qui fait face à deux
guerriers Barbares. Il est en train de passer un Bracelet d'Or au
poignet de l'un d'eux et, de toute évidence, il ne s'est pas aperçu
de votre présence. Il n'existe pas d'escalier permettant de
descendre dans la salle où se trouve Vonotar; en revanche, vous
découvrez une porte au bout du balcon.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez une Corde, vous pouvez vous en servir pour descendre du balcon et tenter de capturer Vonotar ; rendez-vous alors au :"))
    if has_item("CORDE"):
        st.page_link("tomes/tome3/page_100.py", label="100", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome3/page_100.py", label="100", icon="📄", disabled=True)
    st.write_stream(stream_text("Si vous n'avez pas de Corde, vous pouvez redescendre l'escalier en colimaçon en vous rendant au :"))
    if not has_item("CORDE"):
        st.page_link("tomes/tome3/page_148.py", label="148", icon="📄")
    else:
        st.write_stream(stream_text(fr_has_rope))
        st.page_link("tomes/tome3/page_148.py", label="148", icon="📄", disabled=True)
    st.write_stream(stream_text("Enfin, si vous préférez examiner la porte, au bout du balcon, rendez-vous au :"))
    st.page_link("tomes/tome3/page_61.py", label="61", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
