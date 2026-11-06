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

check_inventory(current_page_number=262, book=6)

fr_text = """
Le Kloon à peau verte vous dévisage, un demi-sourire ironique se
dessinant sur ses épaisses lèvres rouges. « Attendez-moi ici »,
dit-il sèchement puis il quitte la pièce en claquant la porte
derrière lui.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez attendre son retour, rendez-vous au :"))
    st.page_link("tomes/tome6/page_116.py", label="116", icon="📄")

    st.write_stream(stream_text("Si vous préférez quitter la Maison de la Guilde et poursuivre votre chemin, rendez-vous au :"))
    st.page_link("tomes/tome6/page_105.py", label="105", icon="📄")

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de l'Intuition, rendez-vous au :"))
    if has_magnakai("Intuition"):
        st.page_link("tomes/tome6/page_58.py", label="58", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome6/page_58.py", label="58", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
