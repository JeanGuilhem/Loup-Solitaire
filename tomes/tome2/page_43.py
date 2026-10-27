import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=43, book=2)

fr_text = """
Vous faites tournoyer le Glaive de Sommer d'un geste vigoureux et
vous fauchez d'un coup quatre zombies, mais à peine leurs cadavres se
sont-ils écroulés sur le pont que d'autres morts vivants viennent prendre
leur place. Vous ne parviendrez jamais à les tuer tous et vous
succomberez sous le nombre. Ils agrippent votre cape qu'ils
commencent à déchirer et vous n'avez plus qu'à sauter par-dessus bord
pour échapper à une mort certaine.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_286.py", label="286", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
