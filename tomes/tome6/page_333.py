import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=333, book=6)

fr_text = """
Au moment où vous allez donner la Pièce d'Or à la femme, un
homme surgit à ses côtés et, d'une main gantée de fer, lui écrase
les doigts en grognant : « Allez, du vent, sale voleuse ! » La
femme se masse la main endolorie et jette à l'homme un regard
noir.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si cette scène vous a indigné au point de vous battre avec cet homme, rendez-vous au :'))
    st.page_link("tomes/tome6/page_71.py", label="71", icon="📄")

    st.write_stream(stream_text('Si vous souhaitez lui demander des explications, rendez-vous au :'))
    st.page_link("tomes/tome6/page_154.py", label="154", icon="📄")

    st.write_stream(stream_text('Enfin, si vous optez pour une fuite qui épargnera tout affrontement, rendez-vous au :'))
    st.page_link("tomes/tome6/page_279.py", label="279", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
