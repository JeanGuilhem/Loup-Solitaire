import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

fr_unknown_item = "Vous ne possédez pas cet objet."

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=169, book=3)

fr_text = """
Lorsque vous arrivez devant la porte massive, vous essayez
désespérément de trouver un moyen de l'ouvrir, mais elle est
parfaitement lisse et ne comporte ni poignée, ni serrure, ni trou
de serrure. La créature aura bientôt atteint le sommet de la
rampe et vous êtes sur le point de pousser un cri de désespoir
lorsque vous apercevez un bloc de granit encastré dans le mur.
Un petit triangle est gravé dans la pierre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous possédez un Triangle de Pierre Bleue, rendez-vous au :'))
    if has_item("TRIANGLE DE PIERRE BLEUE"):
        st.page_link("tomes/tome3/page_41.py", label="41", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome3/page_41.py", label="41", icon="📄", disabled=True)
    st.write_stream(stream_text('Sinon, rendez-vous au :'))
    st.page_link("tomes/tome3/page_265.py", label="265", icon="📄", disabled=has_item("TRIANGLE DE PIERRE BLEUE"))

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
