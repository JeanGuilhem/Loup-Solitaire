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

check_inventory(current_page_number=292, book=6)

fr_text = """
Votre flèche empennée fend l'air puis s'enfonce profondément dans
l'épaule de la créature. Elle hurle de douleur puis, d'un coup de
patte, casse la flèche en deux. Bien que vous l'ayez grièvement
blessée, la bête est loin d'être à l'agonie. Elle passe à
l'attaque et essaie de vous atteindre au visage avec ses griffes
acérées couvertes de sang, mais vous plongez juste à temps pour
éviter d'être décapité. Vous vous relevez rapidement, prêt à
affronter la créature.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_343.py", label="343", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
