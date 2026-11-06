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

check_inventory(current_page_number=116, book=6)

fr_text = """
La porte s'ouvre brusquement et un chien de guerre à l'aspect
féroce fait irruption dans la pièce. « Le dîner est servi,
Brutus, régale-toi ! » crie le Kloon d'un air ravi. A ces mots,
le molosse s'élance sur vous et tente de vous saisir à la gorge.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # fuite possible au premier Assaut seulement : le bouton disparaît une fois le premier Assaut joué
    first_round = st.session_state.get("combat_combat", {}).get("round", 0) == 0
    outcome = combat([("BRUTUS LE CHIEN DE GUERRE", 17, 25)], flee_after=0 if first_round else None)
    if outcome == "fled":
        st.write_stream(stream_text("Vous ne pouvez esquiver l'attaque qu'au premier Assaut seulement, en sortant de la pièce et en fuyant par l'escalier donnant sur la rue. Si tel est votre choix, rendez-vous au :"))
        st.page_link("tomes/tome6/page_105.py", label="105", icon="📄")
    elif outcome == "win":
        st.write_stream(stream_text("Si vous sortez vainqueur de la lutte, rendez-vous au :"))
        st.page_link("tomes/tome6/page_193.py", label="193", icon="📄")
    elif outcome is None and first_round:
        st.caption("Vous ne pouvez esquiver l'attaque qu'au premier Assaut, en fuyant par l'escalier (rendez-vous alors au 105).")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
