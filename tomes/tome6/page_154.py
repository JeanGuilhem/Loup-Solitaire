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

check_inventory(current_page_number=154, book=6)

fr_text = """
L'homme saisit vivement la malheureuse par le poignet et, d'un
geste brusque, découvre le bébé qu'elle berçait dans ses bras : la
mère indigne cachait sous la couverture une longue épingle dont
elle piquait l'enfant pour le faire pleurer à volonté ! « Vous finirez
mendiant à votre tour si vous vous laissez prendre aux ruses de
ce genre de femme », vous dit l'homme. D'un geste rageur, la
misérable se dégage de sa poigne et disparaît rapidement dans la
foule en maugréant. « Vous êtes au service de qui ? reprend
l'homme au visage rude, encadré d'une barbe noire bien taillée.
Mais peut-être cherchez-vous à vous faire enrôler, hein ? »
poursuit-il.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez engager la conversation avec cet homme, rendez-vous au :"))
    st.page_link("tomes/tome6/page_181.py", label="181", icon="📄")

    st.write_stream(stream_text("Si vous préférez partir sans plus tarder, rendez-vous au :"))
    st.page_link("tomes/tome6/page_279.py", label="279", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
