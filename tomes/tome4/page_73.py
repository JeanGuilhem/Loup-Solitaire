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

check_inventory(current_page_number=73, book=4)

fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
Vous vous approchez de l'autel dans un mouvement tournant en
restant hors de portée du poignard à la lame enflammée. De son
autre main, Barraka dégaine alors son cimeterre et tente de vous
frapper de sa lame brillante comme un miroir. Il vous rate
cependant.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez un flacon d'Eau Bénite, rendez-vous au :"))
    if has_item("EAU BÉNITE"):
        st.page_link("tomes/tome4/page_283.py", label="283", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome4/page_283.py", label="283", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous possédez le Glaive de Sommer, rendez-vous au :"))
    if has_item("GLAIVE DE SOMMER"):
        st.page_link("tomes/tome4/page_325.py", label="325", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome4/page_325.py", label="325", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous ne possédez ni l'un ni l'autre, rendez-vous au :"))
    st.page_link("tomes/tome4/page_122.py", label="122", icon="📄", disabled=has_item("EAU BÉNITE") or has_item("GLAIVE DE SOMMER"))

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
