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

check_inventory(current_page_number=20, book=5)

fr_text = """
Le guerrier tire avec frénésie sur les rênes en essayant de vous
piétiner sous les sabots de son cheval effarouché.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    fight = st.session_state.get("combat_cavalier")
    if not fight or fight["status"] == "setup":
        st.write_stream(stream_text('Si vous préférez vous rendre pour éviter le combat, rendez-vous au :'))
        st.page_link("tomes/tome5/page_176.py", label="176", icon="📄")
    st.write_stream(stream_text("Vous pouvez arrêter le combat à tout moment en plongeant dans la mer (bouton de fuite)."))
    # « Si vous perdez le combat » : le Cavalier voulait seulement vous assommer
    outcome = combat([("CAVALIER", 21, 28)], key="cavalier", flee_after=0, max_rounds=3, knockout=True)
    if outcome == "win":
        st.write_stream(stream_text('Si vous sortez vainqueur, en 3 Assauts ou moins, rendez-vous au :'))
        st.page_link("tomes/tome5/page_125.py", label="125", icon="📄")
    elif outcome == "rounds_over":
        st.write_stream(stream_text('Si le combat dure plus de 3 Assauts, rendez-vous au :'))
        st.page_link("tomes/tome5/page_82.py", label="82", icon="📄")
    elif outcome == "fled":
        st.write_stream(stream_text('Vous plongez dans la mer. Rendez-vous au :'))
        st.page_link("tomes/tome5/page_142.py", label="142", icon="📄")
    elif outcome == "lost":
        st.write_stream(stream_text('Si vous perdez le combat, rendez-vous au :'))
        st.page_link("tomes/tome5/page_161.py", label="161", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
