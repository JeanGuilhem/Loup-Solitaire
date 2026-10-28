import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=147, book=3)

fr_text = """
Vous inspectez chaque centimètre carré de la porte et des murs
qui l'encadrent, mais vous ne trouvez strictement rien qui puisse
permettre de l'ouvrir. Vous examinez alors la rampe de pierre
lorsqu'un rugissement retentit soudain derrière vous avec tant de
force que votre sang se glace. Vous faites volte-face et vous voyez
alors une créature bondir sur vous : ses mâchoires grandes
ouvertes laissent apercevoir une langue couverte de poils rêches.
Il vous est impossible d'échapper à ce Languabarb et il vous faut
le combattre jusqu'à la mort de l'un de vous deux.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("LANGUABARB", 10, 28)], stop_when_wounded=True)
    if outcome == "wounded":
        st.write_stream(stream_text("Vous avez perdu des points d'ENDURANCE au cours de l'affrontement : rendez-vous immédiatement au :"))
        st.page_link("tomes/tome3/page_66.py", label="66", icon="📄")
    elif outcome == "win":
        st.write_stream(stream_text("Vous remportez la victoire sans perdre un seul point d'ENDURANCE : rendez-vous au :"))
        st.page_link("tomes/tome3/page_84.py", label="84", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
