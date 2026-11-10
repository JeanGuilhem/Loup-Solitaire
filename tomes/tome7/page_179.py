import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    magnakai_rank,
    show_illustrations,
    show_map,
)
from text import fr_unknown_magnakai
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=179, book=7)

fr_text = """
Grâce à votre Discipline Magnakaï, vous parvenez à bloquer
l'attaque psychique, soulageant ainsi la douleur qui vous vrillait
la tête. Mais la main a senti votre résistance. Repliant ses doigts
en un grotesque poing, elle se met à marteler le socle à coups
lents et puissants. Des ondes de choc viennent frapper votre
Écran Psychique et vous devez lutter de toutes vos forces pour
l'empêcher de céder.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # rang de Maître Primat : 4 Disciplines Magnakaï
    psi_surge = has_magnakai("Foudroiement Psychique") and magnakai_rank() >= 4

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï du Foudroiement Psychique et que vous avez atteint le rang Kaï de Maître Primat, rendez-vous au :"))
    if psi_surge:
        st.page_link("tomes/tome7/page_134.py", label="134", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome7/page_134.py", label="134", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous ne maîtrisez pas la Discipline Magnakaï du Foudroiement Psychique, ou si vous n'avez pas atteint le rang de Maître Primat, rendez-vous au :"))
    st.page_link("tomes/tome7/page_297.py", label="297", icon="📄", disabled=psi_surge)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
