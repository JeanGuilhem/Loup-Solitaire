import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    kai_rank,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=118, book=5)

fr_text = """
Le Garde porte la sarbacane à ses lèvres. Ses joues se gonflent et
un sifflement aigu vous avertit qu'une autre fléchette
empoisonnée se dirige rapidement vers votre tête.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous avez atteint le rang de Guerrier Kaï (ou un rang plus élevé), ajoutez 1 au chiffre obtenu."))
    roll = hazard_roll()
    if roll is not None:
        bonus = 1 if kai_rank() >= 8 else 0
        total = roll + bonus
        if bonus:
            st.write(f"*Rang de Guerrier Kaï : +1, soit un total de {total}.*")
        if total <= 3:
            st.write_stream(stream_text("Si votre total est compris entre 0 et 3, rendez-vous au :"))
            st.page_link("tomes/tome5/page_89.py", label="89", icon="📄")
        else:
            st.write_stream(stream_text("S'il est compris entre 4 et 12, rendez-vous au :"))
            st.page_link("tomes/tome5/page_21.py", label="21", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
