import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_flag,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=107, book=3)

fr_text = """
Lorsque vous jetez un regard dans la vaste caverne de glace, un
peu plus loin, vous apercevez avec horreur trois grosses créatures
à l'aspect repoussant qui sont en train de se battre en échangeant
des coups de griffes. elles se disputent une carcasse déchirée,
étalée sur le sol. Ces créatures sont des Languabarbs, de
sauvages prédateurs du pays de Kalte.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if has_flag("huile de Bakanal"):
        st.write_stream(stream_text("Si vous vous êtes enduit la peau d'huile de Bakanal, rendez-vous au :"))
        st.page_link("tomes/tome3/page_202.py", label="202", icon="📄")
    else:
        st.write_stream(stream_text("Si vous vous êtes enduit la peau d'huile de Bakanal, rendez-vous au :"))
        st.write_stream(stream_text("Vous ne vous êtes pas enduit d'huile de Bakanal."))
        st.page_link("tomes/tome3/page_202.py", label="202", icon="📄", disabled=True)
        st.write_stream(stream_text("Si vous n'êtes pas imprégné d'huile de Bakanal, vous pouvez éviter les Languabarbs en revenant sur vos pas, en direction de l'autre tunnel. Rendez-vous pour cela au :"))
        st.page_link("tomes/tome3/page_284.py", label="284", icon="📄")
    st.write_stream(stream_text("Si enfin vous souhaitez attaquer les trois créatures, rendez-vous au :"))
    st.page_link("tomes/tome3/page_138.py", label="138", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
