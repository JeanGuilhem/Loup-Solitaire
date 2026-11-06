import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=249, book=6)

fr_text = """
Il y a un grand trou au milieu des barres de la grille par lequel
vous pouvez vous faufiler facilement. Les eaux fétides filtrées par
cette grille charrient toutes sortes d'immondices, véritable festin
pour les rats et la vermine qui doivent grouiller dans cet égout.
Mais, au fur et à mesure que vous progressez dans ce tunnel,
vous vous rendez compte qu'il n'y a aucun rat et, contrairement à
ce que vous pensiez, il semble complètement dépourvu de toute
trace de vie. A intervalles réguliers, des chutes d'eau tombent du
plafond carrelé, mais les ouvertures sont beaucoup trop petites et
glissantes pour que vous essayiez de les escalader. Vous êtes dans
l'égout depuis un quart d'heure lorsque vous arrivez à un grand
embranchement d'où partent deux nouveaux canaux, qui vont se
jeter dans le grand canal collecteur.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez continuer tout droit, rendez-vous au :"))
    st.page_link("tomes/tome6/page_269.py", label="269", icon="📄")

    st.write_stream(stream_text("Si vous souhaitez suivre le canal gauche, rendez-vous au :"))
    st.page_link("tomes/tome6/page_318.py", label="318", icon="📄")

    st.write_stream(stream_text("Si vous souhaitez suivre le canal droit, rendez-vous au :"))
    st.page_link("tomes/tome6/page_339.py", label="339", icon="📄")

    st.write_stream(stream_text("Enfin, si vous possédez la carte de Tekaro, rendez-vous au :"))
    if has_item("CARTE DE TEKARO") or has_item("PLAN DE TEKARO"):
        st.page_link("tomes/tome6/page_235.py", label="235", icon="📄")
    else:
        st.write("*Vous ne possédez pas la carte de Tekaro.*")
        st.page_link("tomes/tome6/page_235.py", label="235", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
