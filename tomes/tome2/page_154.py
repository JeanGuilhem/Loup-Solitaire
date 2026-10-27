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

check_inventory(current_page_number=154, book=2)

fr_text = """
Dans leur poste d'équipage, les hommes du Sceptre Vert sont entassés
les uns sur les autres; il règne là une atmosphère étouffante,
surchauffée. Mais, en dépit du manque d'espace et de la frugalité du
repas (une frugalité telle qu'elle vous coûte 2 points d'ENDURANCE),
les marins sont contents que vous ayez accepté leur invitation et ils
vous traitent comme un hôte d'honneur. Après dîner, ils vous invitent à
jouer avec eux aux « Hublots ». Il s'agit d'un jeu de dés où l'on mise un
peu d'or.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-2)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)

    st.write_stream(stream_text("Si vous voulez tenter votre chance, rendez-vous au :"))
    st.page_link("tomes/tome2/page_308.py", label="308", icon="📄")

    st.write_stream(
        stream_text(
            "Si vous préférez décliner leur offre et leur souhaiter bonne nuit avant de regagner votre "
            "cabine, rendez-vous au :"
        )
    )
    st.page_link("tomes/tome2/page_197.py", label="197", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
