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

check_inventory(current_page_number=309, book=2)

fr_text = """
Lorsque vous avancez sur le pont, les hideuses créatures font volte-face
et s'enfuient devant la clarté d'or de votre Glaive. Ce vaisseau fantôme
vous semble alors étrange, il vous rappelle quelque chose de familier,
mais vous ne savez pas quoi exactement. Puis soudain, une voix
sépulcrale retentit derrière vous en vous appelant par votre nom. Vous
vous retournez en brandissant le Glaive de Sommer et une vision
terrifiante vous glace alors le sang.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_26.py", label="26", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
