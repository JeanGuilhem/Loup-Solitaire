import streamlit as st
from combat import combat
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

check_inventory(current_page_number=198, book=4)

fr_text = """
Les Gardes ne se laissent pas prendre à votre stratagème. Ils
tirent aussitôt leur épée et se lancent à l'attaque. Il vous faut les
combattre en les considérant comme un seul et même ennemi.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("GARDES DE LA CRYPTE", 18, 30)])
    if outcome == "win":
        st.write_stream(stream_text('Si vous êtes vainqueur, rendez-vous au :'))
        st.page_link("tomes/tome4/page_229.py", label="229", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
