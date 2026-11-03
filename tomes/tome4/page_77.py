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

check_inventory(current_page_number=77, book=4)

fr_text = """
Un rictus cruel déforme son visage repoussant. Vous l'entendez
parler dans votre tête, bien que ses lèvres restent immobiles : ce
Guerrier est doté d'une puissante force mentale. Si vous ne
maîtrisez pas la Discipline Kaï du Bouclier Psychique, vous
perdrez 1 point d'ENDURANCE supplémentaire à chaque Assaut
au cours du combat que vous livrerez contre lui. Votre adversaire
est invulnérable à votre propre Puissance Psychique.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Vous aurez le droit de prendre la fuite après avoir mené au moins 2 Assauts."))
    outcome = combat([("CAPITAINE VASSAGONIEN", 22, 28)], psychic_immune=True, psychic_damage=1, flee_after=2)
    if outcome == "fled":
        st.write_stream(stream_text("Si vous prenez la fuite, rendez-vous au :"))
        st.page_link("tomes/tome4/page_98.py", label="98", icon="📄")
    elif outcome == "win":
        st.write_stream(stream_text("Si vous sortez vainqueur du combat, rendez-vous au :"))
        st.page_link("tomes/tome4/page_10.py", label="10", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
