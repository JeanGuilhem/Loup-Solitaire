import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_discipline,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=233, book=7)

fr_text = """
Le ver avance inexorablement, vous obligeant à reculer le long de
la rampe jusqu'à la porte ovale. Mais vous n'avez aucune
possibilité de fuir de ce côté-là et vous devez combattre cette
créature répugnante. Le monstre est particulièrement sensible
aux attaques psychiques et, si vous décidez d'avoir recours à la
Puissance Psychique ou au Foudroiement Psychique, doublez
tous les points d'ENDURANCE que perd votre ennemi au cours
du combat.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # La Puissance Psychique est toujours employée par le moteur (+2, ou Foudroiement +4 si activé) :
    # le héros qui la possède double donc les pertes du ver.
    psychic = has_discipline("Puissance psychique", "Foudroiement Psychique")
    outcome = combat([("OUDAGORG", 17, 17)], enemy_loss_multiplier=2 if psychic else 1)
    if outcome == "win":
        st.write_stream(stream_text("Si vous remportez la bataille, rendez-vous au :"))
        st.page_link("tomes/tome7/page_209.py", label="209", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
