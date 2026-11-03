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

check_inventory(current_page_number=184, book=4)

fr_text = """
Vous êtes à 10 mètres à peine des Gardes lorsqu'ils se mettent à
tirer. Par miracle, vous n'êtes pas touché, mais il vous faudra
désormais combattre seul. Trois de vos hommes viennent en
effet d'être tués ; quant au quatrième, un carreau d'arbalète lui a
fracassé le poignet et il est désormais hors de combat. Lorsque
vous les attaquez, les féroces Guerriers se débarrassent de leurs
arbalètes vides et tirent leurs épées. Vous êtes alors repoussé en
direction du pont par six Gardes furieux.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez les combattre, rendez-vous au :'))
    st.page_link("tomes/tome4/page_202.py", label="202", icon="📄")

    st.write_stream(stream_text('Si vous préférez vous enfuir en sautant par-dessus le parapet du pont, rendez-vous au :'))
    st.page_link("tomes/tome4/page_342.py", label="342", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
