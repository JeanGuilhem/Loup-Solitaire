import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=261, book=6)

fr_text = """
Vous éperonnez vigoureusement les flancs de votre cheval et, en
l'espace de quelques secondes, vous traversez les rangs des gardes
médusés. Vous vous dirigez au grand galop vers la porte, lorsque
deux sentinelles surgissent et vous bloquent le passage. Ils sont
armés de longues piques qu'ils pointent sur votre poitrine. Vous
tirez fermement sur les rênes pour éviter les menaçantes pointes
d'acier.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous maîtrisez la Discipline Magnakaï du Contrôle Animal, ajoutez 3 au chiffre que vous avez obtenu."))
    roll = hazard_roll(key="t6_261")
    if roll is not None:
        bonus = 3 if has_magnakai("Contrôle Animal") else 0
        total = roll + bonus
        if bonus:
            st.write(f"*Contrôle Animal : +3, soit un total de {total}.*")
        if total <= 2:
            st.write_stream(stream_text("Si votre total est compris entre 0 et 2, rendez-vous au :"))
            st.page_link("tomes/tome6/page_99.py", label="99", icon="📄")
        elif total <= 6:
            st.write_stream(stream_text("S'il est compris entre 3 et 6, rendez-vous au :"))
            st.page_link("tomes/tome6/page_187.py", label="187", icon="📄")
        else:
            st.write_stream(stream_text("S'il est égal ou supérieur à 7, rendez-vous au :"))
            st.page_link("tomes/tome6/page_22.py", label="22", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
