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

check_inventory(current_page_number=227, book=5)

fr_text = """
Tandis que vous vous approchez d'une allée plongée dans
l'obscurité, vous entendez la voix d'une vieille femme qui mendie
dans l'ombre. « Ayez pitié jeunes gens ! Ayez pitié d'une pauvre
veuve ! » Une vieille femme décrépite apparaît à la lumière, le
visage tout ridé et les yeux hagards. Elle répète sa complainte, les
traits crispés. « A vot'bon cœur, M'sieurs-dames, pour une
pauvre veuve dans l'besoin. »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous désirez vous arrêter pour la questionner, rendez-vous au :"))
    st.page_link("tomes/tome5/page_265.py", label="265", icon="📄")

    st.write_stream(stream_text("Si vous préférez passer votre chemin, sans vous soucier de la vieille femme, rendez-vous au :"))
    st.page_link("tomes/tome5/page_388.py", label="388", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
