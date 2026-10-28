import streamlit as st
from combat import combat_weapons
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    is_mastered,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=86, book=3)

fr_text = """
Vous introduisez l'extrémité de votre lame dans le trou de la
serrure en essayant d'actionner le mécanisme d'ouverture. La
gorge de la serrure est cependant très profonde et il vous est
difficile de parvenir à vos fins.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            "Utilisez la Table de Hasard pour obtenir un chiffre. Si vous possédez la Discipline Kaï de la "
            "Maîtrise des Armes et qu'elle s'applique précisément à l'arme que vous êtes en train d'utiliser, "
            "vous aurez le droit d'ajouter 3 au chiffre obtenu."
        )
    )
    weapons = combat_weapons()
    weapon = None
    if weapons:
        weapon = st.selectbox(
            "Arme que vous utilisez pour forcer la serrure :",
            weapons,
            key="lock_weapon",
            disabled="hazard_hazard" in st.session_state,
        )
    roll = hazard_roll()
    if roll is not None:
        bonus = 3 if weapon and is_mastered(weapon) else 0
        total = roll + bonus
        if bonus:
            st.write(f"*Votre Maîtrise des Armes vous donne +{bonus} : total {total}.*")
        if total <= 7:
            st.write_stream(stream_text("Le total se situe entre 0 et 7, rendez-vous au :"))
            st.page_link("tomes/tome3/page_47.py", label="47", icon="📄")
        else:
            st.write_stream(stream_text("Le total se situe entre 8 et 12, rendez-vous au :"))
            st.page_link("tomes/tome3/page_194.py", label="194", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
