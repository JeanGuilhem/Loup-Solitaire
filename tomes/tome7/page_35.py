import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    magnakai_rank,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=35, book=7)

fr_text = """
Par un extraordinaire effort de volonté, vous parvenez à calmer
la douleur qui vous martèle les tempes et vous essayez d'obliger
la Sphère à cesser son Attaque Psychique.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # le livre oublie le 5 (« entre 0 et 4 » / « supérieur à 5 ») : 5 et plus mènent au 246
    bonus = 1 if magnakai_rank() >= 4 else 0  # rang de Maître primat
    roll = hazard_roll(label="Utilisez la Table de Hasard (+1 si vous avez atteint le rang de Maître Primat).")
    if roll is not None:
        total = roll + bonus
        if bonus:
            st.write(f"*{roll} + 1 (Maître Primat) = {total}.*")
        if total <= 4:
            st.write_stream(stream_text('Si le résultat obtenu est compris entre 0 et 4, rendez-vous au :'))
            st.page_link("tomes/tome7/page_97.py", label="97", icon="📄")
        else:
            st.write_stream(stream_text('Si ce résultat est supérieur à 5, rendez-vous au :'))
            st.page_link("tomes/tome7/page_246.py", label="246", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
