import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    is_new_page,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=280, book=3)

fr_text = """
La Clé est recouverte d'un suc digestif particulièrement acide qui
transperce vos moufles et vous brûle les doigts. Vous perdez 1
point d'ENDURANCE. Lâchant aussitôt la Clé, vous plongez vos
mains dans la neige pour calmer la douleur. Si vous tenez quand
même à conserver cette Clé, essuyez-la dans la neige avant de la
glisser dans votre poche, et inscrivez-la sur votre Feuille
d'Aventure dans la case Objets Spéciaux. Il vous faut à présent
trouver le moyen d'ouvrir la porte de la forteresse.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-1)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-1)

    if not has_item("CLÉ D'ARGENT"):
        pickup_button("CLÉ D'ARGENT", key="cle_argent", label="Essuyer la Clé d'Argent et la garder")

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome3/page_344.py", label="344", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
