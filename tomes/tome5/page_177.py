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

check_inventory(current_page_number=177, book=5)

fr_text = """
Tandis que vous assénez un coup mortel au Kwaraz, trois
Sharnazims émergent avec difficulté des eaux sombres de l'égout.
Ils ont enlevé leur tunique noire et ils arborent sur leur torse
musclé un tatouage bleu représentant les serres d'un aigle. Une
fois hors de l'eau, ils dégainent leur cimeterre à la lame
tranchante comme un rasoir tout en vous fixant d'un œil
mauvais.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez attaquer les Sharnazims, rendez-vous au :'))
    st.page_link("tomes/tome5/page_60.py", label="60", icon="📄")

    st.write_stream(stream_text("Si vous préférez fuir par l'étroit escalier de pierre, rendez-vous au :"))
    st.page_link("tomes/tome5/page_43.py", label="43", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
