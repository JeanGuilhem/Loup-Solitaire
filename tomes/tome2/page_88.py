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

check_inventory(current_page_number=88, book=2)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Bien que la nuit soit tombée, la pleine lune projette une brillante clarté
sur tout le village. Derrière la taverne, vous apercevez la petite boutique
d'un charron ; deux chevaux sont attelés à une charrette à foin
stationnée juste devant la porte.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            "Si vous souhaitez prendre l'un des chevaux pour vous enfuir au galop, rendez-vous au :"
        )
    )
    st.page_link("tomes/tome2/page_150.py", label="150", icon="📄")

    st.write_stream(stream_text("Si vous préférez vous cacher dans la boutique du charron, rendez-vous au :"))
    st.page_link("tomes/tome2/page_71.py", label="71", icon="📄")

    st.write_stream(stream_text("Si enfin vous maîtrisez la Discipline Kaï du Camouflage, rendez-vous au :"))
    if has_kai("Le Camouflage"):
        st.page_link("tomes/tome2/page_179.py", label="179", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome2/page_179.py", label="179", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
