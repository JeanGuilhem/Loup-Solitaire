import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    remove_from_inventory,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=321, book=5)

fr_text = """
Vous posez l'herbe d'Oede à l'entrée du pont de pierre et vous
reculez. Tout d'abord, le lépreux reste méfiant et effrayé, car
personne n'a osé entrer dans sa grotte depuis fort longtemps.
Mais dès qu'il reconnaît les feuilles dorées de l'herbe d'Oede, il
s'effondre en versant des larmes de joie. «Que le Majhan vous
bénisse ! Puissiez-vous vivre en paix éternelle ! s'écrie-t-il, la voix brisée par l'émotion. Comment pourrai-je jamais vous remercier?»
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        remove_from_inventory("HERBE D'OEDE")
    st.caption("Vous avez donné votre herbe d'Oede au lépreux.")

    st.write_stream(stream_text('Si vous désirez interroger le lépreux au sujet de Tipasa le Vagabond, rendez-vous au :'))
    st.page_link("tomes/tome5/page_356.py", label="356", icon="📄")

    st.write_stream(stream_text('Si vous préférez quitter la grotte et vous remettre en route pour Ikaresh sans plus tarder, rendez-vous au :'))
    st.page_link("tomes/tome5/page_281.py", label="281", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
