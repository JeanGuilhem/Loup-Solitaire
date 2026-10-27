import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=344, book=2)

fr_text = """
Votre Sixième Sens vous révèle que ces étrangers sont des Monstres
d'Enfer, les féroces serviteurs des Maîtres des Ténèbres, et qu'ils ont
pour mission de vous assassiner. Ces immondes créatures ont le
pouvoir de prendre à leur guise une apparence humaine et sont par
ailleurs invulnérables aux armes habituelles tout autant qu'à la
Puissance Psychique. Vous criez à Rhygar et à ses hommes de prendre
garde à ces monstres, puis vous vous enfuyez vers la forêt.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_183.py", label="183", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
