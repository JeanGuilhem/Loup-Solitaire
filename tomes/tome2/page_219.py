import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=219, book=2)

fr_text = """
Le venin commence à faire son effet. Votre bras mordu s'engourdit et
une sueur froide perle à votre front. Vous ôtez aussitôt de votre cou le
pendentif que Banedon vous a donné dans les Ruines de Raumas et à
l'aide d'une des pointes de l'étoile de cristal, vous incisez la peau de
votre bras à l'endroit de la morsure. Vous posez ensuite vos lèvres sur
la plaie et vous aspirez le venin. Le porte-bonheur se révèle efficace et
la chance est avec vous, car vous survivez à la morsure, bien que vous
perdiez 3 points d'ENDURANCE. Vous décidez ensuite de grimper
dans l'arbre et de passer le reste de la nuit à l'abri de son feuillage, à
bonne distance du sol.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-3)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-3)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome2/page_312.py", label="312", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
