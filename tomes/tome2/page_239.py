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

check_inventory(current_page_number=239, book=2)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Vous essayez d'appliquer la paume de vos mains sur la poitrine de
l'homme blessé, mais les Squalls tirent sur les pans de votre cape pour
vous éloigner de lui.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous maîtrisez la Discipline Kaï du Camouflage, rendez-vous au :'))
    if has_kai('Le Camouflage'):
        st.page_link("tomes/tome2/page_77.py", label="77", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome2/page_77.py", label="77", icon="📄", disabled=True)

    st.write_stream(stream_text('Sinon, il vous faudra attaquer les Squalls pour pouvoir ensuite vous occuper du blessé ; rendez-vous alors au :'))
    st.page_link("tomes/tome2/page_28.py", label="28", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
