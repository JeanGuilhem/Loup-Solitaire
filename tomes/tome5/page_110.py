import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=110, book=5)

fr_text = """
Un reptile gigantesque s'est accroché au plafond à l'aide de ses
longues griffes recourbées. Ses énormes yeux ovales roulent en
tous sens à la vue de chair fraîche, votre propre chair ! Il prépare
son attaque et vous n'avez pas la possibilité de fuir. Menez le
combat.
Cet immense reptile est très sensible au pouvoir psychique, si
vous maîtrisez la Discipline Kaï de la Puissance Psychique,
ajoutez 4 points d'HABILETÉ au lieu des 2 points habituels.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # Puissance psychique : +4 au lieu de +2 (les 2 habituels sont comptés par combat())
    outcome = combat(
        [("KWARAZ", 19, 30)],
        hability_modifier=2 if has_kai("Puissance psychique") else 0,
    )
    if outcome == "win":
        st.write_stream(stream_text("Si vous sortez vainqueur, rendez-vous au :"))
        st.page_link("tomes/tome5/page_40.py", label="40", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
