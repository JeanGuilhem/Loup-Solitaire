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

check_inventory(current_page_number=146, book=5)

fr_text = """
Pendant quelques minutes, vous regardez l'homme travailler à
son enclume, au cas où lui aussi déciderait de quitter la pièce.
Mais il continue à forger, apparemment peu affecté par la
chaleur torride qui règne dans ces lieux. Pour atteindre la porte
ouest sans être vu, vous devez traverser prudemment la forge en
passant d'un pilier à un autre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous maîtrisez la Discipline Kaï du Camouflage ou de la Chasse, ôtez 2 au chiffre obtenu."))
    roll = hazard_roll()
    if roll is not None:
        malus = 2 if has_kai("Le Camouflage") or has_kai("La Chasse") else 0
        total = roll - malus
        if malus:
            st.write(f"*Discipline Kaï : -2, soit un total de {total}.*")
        # le livre ne dit rien d'un total de 2 : il est compté avec les totaux inférieurs
        if total <= 2:
            st.write_stream(stream_text("Si votre total est inférieur à 2, rendez-vous au :"))
            st.page_link("tomes/tome5/page_44.py", label="44", icon="📄")
        else:
            st.write_stream(stream_text("Si votre total est égal ou supérieur à 3, rendez-vous au :"))
            st.page_link("tomes/tome5/page_190.py", label="190", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
