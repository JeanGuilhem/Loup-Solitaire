import streamlit as st
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

check_inventory(current_page_number=134, book=5)

fr_text = """
Vous utilisez votre Discipline Kaï pour contraindre la créature à
la fuite. La Sangsue géante change brusquement de direction
puis se précipite sur un calmar qui a trouvé refuge dans une
amphore en cuivre. Vous continuez à nager tout en surveillant la
Sangsue qui vient de dévorer le pauvre calmar après l'avoir
étouffé.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_95.py", label="95", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
