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

check_inventory(current_page_number=230, book=2)

fr_text = """
Vous marchez le long de la voie qui tourne brusquement à l'est pour
aboutir à la rue du Mendiant. Cette artère est d'ailleurs bien nommée
car des dizaines d'hommes, de femmes et d'enfants, tous vêtus de
haillons, s'y rassemblent par groupes, à l'abri des portes cochères, en
tendant des sébiles aux passants. Et tandis que vous suivez l'avenue en
direction d'un croisement, vous êtes assailli de tous côtés par des
miséreux qui vous demandent de l'or.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez leur faire l'aumône, rendez-vous au :"))
    st.page_link("tomes/tome2/page_93.py", label="93", icon="📄")

    st.write_stream(stream_text('Si vous préférez les repousser et poursuivre votre chemin, rendez-vous au :'))
    st.page_link("tomes/tome2/page_137.py", label="137", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
