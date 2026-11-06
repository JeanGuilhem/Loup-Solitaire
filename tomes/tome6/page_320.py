import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    show_illustrations,
    show_map,
)
from text import fr_unknown_magnakai
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=320, book=6)

fr_text = """
Tandis que vous approchez des grandes portes du temple, vous
entendez la voix stridente d'un homme en train de prêcher
devant une congrégation. Ses paroles sont interrompues par
intervalles par le chœur de l'assistance.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez pénétrer dans le temple, rendez-vous au :'))
    st.page_link("tomes/tome6/page_226.py", label="226", icon="📄")

    st.write_stream(stream_text("Si vous préférez inspecter l'observatoire, rendez-vous au :"))
    st.page_link("tomes/tome6/page_127.py", label="127", icon="📄")

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de l'Exploration ou de l'Intuition, rendez-vous au :"))
    if has_magnakai("Exploration") or has_magnakai("Intuition"):
        st.page_link("tomes/tome6/page_195.py", label="195", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome6/page_195.py", label="195", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
