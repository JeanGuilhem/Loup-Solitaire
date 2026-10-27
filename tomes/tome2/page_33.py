import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=33, book=2)

fr_text = """
Les autres voyageurs contemplent d'un air horrifié et incrédule le
résultat du combat que vous venez de livrer. Et avant que vous ayez pu
fournir la moindre explication, la porte de l'auberge s'ouvre
brusquement dans un grand fracas. Six soldats revêtus d'armures se
précipitent à l'intérieur, conduits par l'aubergiste en personne. Les
soldats sont des gardes de la ville et le tenancier borgne les exhorte à
vous arrêter en poussant de grands cris.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez affronter les soldats, rendez-vous au :"))
    st.page_link("tomes/tome2/page_296.py", label="296", icon="📄")
    st.write_stream(stream_text("Si vous préférez vous enfuir par la porte de derrière, rendez-vous au :"))
    st.page_link("tomes/tome2/page_88.py", label="88", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
