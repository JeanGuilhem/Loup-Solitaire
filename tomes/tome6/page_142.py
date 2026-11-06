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

check_inventory(current_page_number=142, book=6)

fr_text = """
Le poignard fend l'air en direction de votre poitrine. Vous vous
jetez à plat ventre sur le pont - mais vos réflexes seront-ils
assez vifs pour esquiver la mortelle lame ? Pour le savoir,
utilisez la Table de Hasard pour obtenir un chiffre. Si vous
maîtrisez la Discipline Magnakaï de Nexus ou de l'Intuition,
réduisez de 3 ce même chiffre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    roll = hazard_roll(key="poignard")
    if roll is not None:
        malus = 3 if has_magnakai("Nexus") or has_magnakai("Intuition") else 0
        total = roll - malus
        if malus:
            st.write(f"*Nexus / Intuition : {roll} - 3 = **{total}**.*")
        st.write_stream(stream_text("Si le résultat obtenu est inférieur ou égal à 4, rendez-vous au :"))
        st.page_link("tomes/tome6/page_184.py", label="184", icon="📄", disabled=total > 4)
        st.write_stream(stream_text("S'il est supérieur ou égal à 5, rendez-vous au :"))
        st.page_link("tomes/tome6/page_51.py", label="51", icon="📄", disabled=total < 5)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
