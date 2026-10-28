import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    kai_rank,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=289, book=3)

fr_text = """
Vous parvenez à ôter la cire et le bouchon sans casser la fiole
dont vous pouvez à présent flairer le contenu.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï de la Communication Animale, ou si vous avez le titre Kaï d'Aspirant, ou un titre supérieur (ce qui signifie que vous maîtrisez au moins 6 Disciplines Kaï), rendez-vous au :"))
    if has_kai("Communication Animale") or kai_rank() >= 6:
        st.page_link("tomes/tome3/page_156.py", label="156", icon="📄")
    else:
        st.write_stream(stream_text("Vous ne maîtrisez pas cette discipline Kaï et vous n'avez pas le titre d'Aspirant."))
        st.page_link("tomes/tome3/page_156.py", label="156", icon="📄", disabled=True)
        st.write_stream(stream_text("L'odeur de moisissure du liquide vous rend méfiant et vous vous débarrassez de la fiole. Retournez à présent au 10 et faites un nouveau choix :"))
        st.page_link("tomes/tome3/page_10.py", label="10", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
