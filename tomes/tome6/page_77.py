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

check_inventory(current_page_number=77, book=6)

fr_text = """
Enjambant les cadavres qui gisent çà et là, vous vous frayez un
chemin vers le pont, où le Capitaine livre bataille à cinq
pirates. Il attaque d'une main avec une longue épée et se défend
de l'autre avec un bouclier en bronze fixé sur son avant-bras
gauche. Il se bat comme un tigre, avec une froide détermination,
ne faisant qu'une bouchée de ces maladroits pirates. Mais le
hurlement rauque d'un cor de guerre retentit soudain, annonçant
l'arrivée d'une nouvelle horde d'assaillants. Anticipant le
danger que court le Capitaine, vous vous élancez à ses côtés
pour lui prêter main-forte et le protéger des pirates ivres de
fureur qui s'apprêtent à le surprendre par-derrière.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Enivrés par la frénésie de la bataille, les Pirates Rouges sont insensibles à la Puissance Psychique mais non au Foudroiement Psychique."))
    outcome = combat([("PIRATES ROUGES", 30, 30)], psychic_power_immune=True)  # sensibles au seul Foudroiement
    if outcome == "win":
        st.write_stream(stream_text("Si vous sortez vainqueur de l'affrontement, rendez-vous au :"))
        st.page_link("tomes/tome6/page_297.py", label="297", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
