import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    receive_gold,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=88, book=6)

fr_text = """
Votre rapide victoire sur les voleurs vous rapporte 5 Pièces
d'Or, que vous trouvez dans leurs poches, ainsi que les regards
respectueux des mercenaires ayant assisté à la scène. L'un de
leurs capitaines se montre particulièrement impressionné par
votre prouesse et il vous propose de venir prendre un verre avec
lui. Vous sentez qu'il s'agit là d'une offre sincère et sans
arrière-pensée, aussi acceptez-vous son invitation de bonne
grâce.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    receive_gold(5, key="t6_88_or")

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_211.py", label="211", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
