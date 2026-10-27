import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=20, book=2)

fr_text = """
Cette rue infestée de rats descend en pente raide en direction des docks
et des embarcadères du Fleuve Dorn. Lorsque vous parvenez sur le
quai, vous apercevez le pont de Ragadorn, le seul et unique lieu de
passage qui relie les rives est et ouest de ce port sordide. Vous vous
frayez un chemin parmi la foule qui se presse sur le pont et vous
empruntez une avenue au sol jonché d'ordures. Elle porte le nom de
Boulevard du Commerce, section Est.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_186.py", label="186", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
