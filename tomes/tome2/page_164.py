import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=164, book=2)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Vous marchez depuis une heure dans ce tunnel désert lorsque vous
apercevez à votre gauche plusieurs marches taillées dans la paroi
rocheuse. Elles mènent à une plateforme qui permet d'atteindre les
torches éclairant le tunnel.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez monter ces marches pour explorer la plate-forme, rendez-vous au :"))
    st.page_link("tomes/tome2/page_52.py", label="52", icon="📄")

    st.write_stream(
        stream_text(
            "Si vous préférez continuer votre chemin sans vous occuper des marches, rendez-vous au :"
        )
    )
    st.page_link("tomes/tome2/page_256.py", label="256", icon="📄")

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï du Sixième Sens, rendez-vous au :"))
    if has_kai("Le Sixième Sens"):
        st.page_link("tomes/tome2/page_172.py", label="172", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome2/page_172.py", label="172", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
