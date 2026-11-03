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

check_inventory(current_page_number=310, book=4)

fr_text = """
Vous êtes à moins de 10 mètres de la tour de guet lorsque la
pointe d'une lance vous projette à terre. Vous roulez de côté juste
à temps pour éviter un coup mortel, puis vous vous relevez d'un
bond face à votre agresseur. C'est un Guerrier au visage dur, les
yeux noirs comme du charbon, son armure éclaboussée par le
sang de son cheval mort. Il lève à nouveau sa lance et s'apprête à
vous frapper en pleine poitrine. Vous n'avez aucune possibilité de
fuir, et il vous faut combattre cet adversaire jusqu'à la mort de
l'un de vous deux.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("GUERRIER VASSAGONIEN", 18, 25)])
    if outcome == "win":
        st.write_stream(stream_text("Si vous remportez la victoire, rendez-vous au :"))
        st.page_link("tomes/tome4/page_24.py", label="24", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
