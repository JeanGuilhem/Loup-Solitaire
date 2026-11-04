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

check_inventory(current_page_number=135, book=5)

fr_text = """
L'air du nouveau tunnel est chaud et humide. Vous continuez
votre progression mais les gaz délétères vous donnent de plus en
plus la nausée et vous êtes bientôt obligé de vous arrêter. Les
vapeurs vous brûlent la gorge et vous donnent des crampes
d'estomac. Soudain, vous entendez derrière vous un bruit qui
vous fait aussitôt oublier vos maux. Vous vous retournez et vous
apercevez, surgissant de l'ombre, un des hommes de Maouk, le
visage protégé par un Masque d'Herbes.
Réduisez votre total d'HABILETÉ de 2 points à cause des fumées
nocives.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # perdre ce combat ne tue pas : le guerrier voulait seulement vous assommer
    outcome = combat([("GUERRIER SHARNAZIM", 17, 22)], hability_modifier=-2, knockout=True)
    if outcome == "win":
        st.write_stream(stream_text("Si vous le gagnez, rendez-vous au :"))
        st.page_link("tomes/tome5/page_130.py", label="130", icon="📄")
    elif outcome == "lost":
        st.write_stream(stream_text("Si vous perdez ce combat, rendez-vous au :"))
        st.page_link("tomes/tome5/page_161.py", label="161", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
