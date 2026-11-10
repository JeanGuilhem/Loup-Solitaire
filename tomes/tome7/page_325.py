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

check_inventory(current_page_number=325, book=7)

fr_text = """
Vous tombez au milieu des vagues et coulez comme une pierre.
L'étreinte glaciale des eaux du lac engourdit vos muscles, et ses
senteurs âcres et piquantes vous remplissent la bouche. Votre
premier réflexe en pénétrant dans l'eau est de nager, mais vous
en êtes empêché par toute une végétation aquatique qui s'enroule
autour de vos membres. Manquant désespérément d'air, vous
essayez rageusement de vous arracher aux algues qui menacent
maintenant de vous entraîner au fond de l'eau. Combattez de la
manière habituelle. Cependant, à cause du manque d'air, vous
devrez automatiquement déduire 2 points d'ENDURANCE à
chaque Assaut.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("ALGUES NOIRES DU LAC", 10, 50)], extra_loss=2)
    if outcome == "win":
        st.write_stream(stream_text("Si vous sortez vivant de cette lutte, rendez-vous au :"))
        st.page_link("tomes/tome7/page_158.py", label="158", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
