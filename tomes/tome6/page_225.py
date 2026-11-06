import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=225, book=6)

fr_text = """
Vous avancez à cheval sous le large porche en pierre de la porte
sud. « Cavalier, sortez votre sauf-conduit ! » crie une voix
hargneuse d'une étroite fente pratiquée dans le mur. Vous
entendez ensuite un verrou grincer bruyamment et deux gardes
en cotte de mailles surgissent à vos côtés. Ils vous dévisagent
d'un œil soupçonneux puis demandent à voir votre sauf-conduit.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez leur dire que vous n'en avez pas, rendez-vous au :"))
    st.page_link("tomes/tome6/page_55.py", label="55", icon="📄")

    st.write_stream(stream_text("Si vous voulez essayer de lancer votre cheval vers la porte ouverte, rendez-vous au :"))
    st.page_link("tomes/tome6/page_261.py", label="261", icon="📄")

    st.write_stream(stream_text("Enfin, si vous préférez tenter de les soudoyer pour entrer dans la ville, rendez-vous au :"))
    st.page_link("tomes/tome6/page_9.py", label="9", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
