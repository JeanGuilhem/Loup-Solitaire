import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=225, book=3)

fr_text = """
Le bouchon est scellé avec de la cire. Si vous voulez briser la cire,
sachez que vous prenez le risque de casser le verre peu épais de la
fiole.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Pour essayer de briser la cire qui scelle le bouchon, rendez-vous au :"))
    st.page_link("tomes/tome3/page_54.py", label="54", icon="📄")
    st.write_stream(
        stream_text(
            "Si le contenu de cette fiole ne vous inspire pas confiance et que vous ne souhaitiez pas risquer "
            "de la casser, abandonnez-la et retournez au :"
        )
    )
    st.page_link("tomes/tome3/page_10.py", label="10", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
