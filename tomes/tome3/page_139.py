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

check_inventory(current_page_number=139, book=3)

fr_text = """
Vous ressentez soudain une douleur sourde et lancinante au côté.
Sous la poche dans laquelle vous avez rangé la Pierre
Rayonnante, votre peau est devenue rouge et enflée. Vous êtes
pris de vertige et de nausées et vous éprouvez de grandes
difficultés à vous maintenir debout.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if has_item("POTION ROUGE DE LAUMSPUR"):
        st.write_stream(stream_text("Si vous possédez une Potion rouge de Laumspur, rendez-vous au :"))
        st.page_link("tomes/tome3/page_116.py", label="116", icon="📄")
    else:
        st.write_stream(stream_text("Si vous possédez une Potion rouge de Laumspur, rendez-vous au :"))
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome3/page_116.py", label="116", icon="📄", disabled=True)
        st.write_stream(stream_text("Dans le cas contraire, rendez-vous au :"))
        st.page_link("tomes/tome3/page_239.py", label="239", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
