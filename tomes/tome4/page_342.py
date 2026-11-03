import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    lose_backpack,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=342, book=4)

fr_text = """
Vous plongez tête la première dans les ténèbres. Le vent vous
siffle aux oreilles. Serrant les dents, vous essayez de ne pas
penser au choc terrible qui vous attend lorsque vous heurterez de
plein fouet le fond rocheux du gouffre. Par chance cependant,
une rivière souterraine coule au-dessous, et vous tombez dedans
en vous enfonçant profondément dans l'eau glacée. Vous
éprouvez un tel soulagement à être encore en vie que vous
oubliez où vous vous trouvez. Vous prenez alors une profonde
inspiration et l'eau pénètre aussitôt dans vos poumons. Essayant
de surmonter la douleur qui vous déchire à présent la poitrine,
vous vous apercevez que votre Sac à Dos vous entraîne vers le
fond. Il faut vous en débarrasser à l'instant, sinon vous serez
noyé. Lorsque vous remontez enfin à la surface, vous nagez tant
bien que mal vers une rive de graviers sur laquelle vous vous
échouez, toussant et haletant. Vous avez perdu votre Sac à Dos et
tout ce qu'il contenait, mais vous êtes vivant et vous n'avez pas
trop souffert.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        lose_backpack()
    st.write("*Vous avez perdu votre Sac à Dos et tout ce qu'il contenait.*")

    st.write_stream(stream_text("Apportez les modifications nécessaires à votre Feuille d'Aventure, puis rendez-vous au :"))
    st.page_link("tomes/tome4/page_219.py", label="219", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
