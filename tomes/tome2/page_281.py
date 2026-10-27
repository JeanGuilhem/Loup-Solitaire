import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=281, book=2)

fr_text = """
Vous demandez avec insistance au capitaine de recueillir les
malheureux naufragés, mais il reste indifférent à vos prières et ordonne
aux hommes d'équipage de poursuivre leurs tâches comme si de rien
n'était. Vous voyez le canot disparaître à l'horizon et vous avez alors la
prémonition qu'un sort semblable vous attend. Troublé par cette pensée,
vous descendez au pont inférieur pour vous retirer dans votre cabine.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome2/page_240.py", label="240", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
