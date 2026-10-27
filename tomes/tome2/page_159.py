import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies, ls_death

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=159, book=2)

fr_text = """
Vous vous arrêtez enfin au pied d'un immense pin et vous essayez de
vous maintenir debout, mais vous avez si mal aux jambes et au côté que
vous tombez par terre en perdant connaissance. Ce sommeil vous
épargne d'être pourfendu par le Monstre d'Enfer, mais il ne vous
sauvera pas de la mort car plus jamais vous ne vous réveillerez. Votre
quête s'achève ici en même temps que votre vie.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    show_illustrations()
    ls_death()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
