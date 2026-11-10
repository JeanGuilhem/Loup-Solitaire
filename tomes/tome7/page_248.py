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

check_inventory(current_page_number=248, book=7)

fr_text = """
Avant même que votre dernier ennemi ait touché le sol, vous
quittez la pièce, puis vous vous enfuyez à toutes jambes le long
du couloir. Vous traversez ensuite un passage voûté qui mène en
haut d'un escalier en colimaçon. Vous descendez rapidement les
marches et vous arrivez à un tunnel orienté est-ouest.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez aller vers l'ouest, rendez-vous au :"))
    st.page_link("tomes/tome7/page_29.py", label="29", icon="📄")

    st.write_stream(stream_text("Si vous préférez aller vers l'est, rendez-vous au :"))
    st.page_link("tomes/tome7/page_272.py", label="272", icon="📄")

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de l'Exploration ou de l'Intuition, rendez-vous au :"))
    if has_magnakai("Exploration") or has_magnakai("Intuition"):
        st.page_link("tomes/tome7/page_171.py", label="171", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome7/page_171.py", label="171", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
