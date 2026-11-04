import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=242, book=5)

fr_text = """
Vous reconnaissez la créature vêtue de rouge : il s'agit d'un
Vordak, l'un des puissants morts vivants au service des Seigneurs
des Ténèbres. Les Vordaks possèdent un pouvoir psychique très
important et vous vous rendez compte qu'il cherche à vous
maîtriser grâce à cette force psychique. Si vous voulez échapper à
ces malfaisants Vordaks, vous devez non seulement protéger
votre corps mais aussi votre esprit.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous maîtrisez la Discipline Kaï du Camouflage, ajoutez 2 points au chiffre que vous avez tiré. Si vous maîtrisez la Discipline Kaï du Bouclier Psychique, ajoutez 3 points à ce chiffre."))
    roll = hazard_roll()
    if roll is not None:
        bonus = 0
        if has_kai("Le Camouflage"):
            bonus += 2
        if has_kai("Bouclier psychique"):
            bonus += 3
        total = roll + bonus
        if bonus:
            st.write(f"*Bonus : +{bonus}, soit un total de {total}.*")
        if total <= 6:
            st.write_stream(stream_text("Si le total obtenu est compris entre 0 et 6, rendez-vous au :"))
            st.page_link("tomes/tome5/page_262.py", label="262", icon="📄")
        else:
            st.write_stream(stream_text("Si le total obtenu est supérieur à 7, rendez-vous au :"))
            st.page_link("tomes/tome5/page_378.py", label="378", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
