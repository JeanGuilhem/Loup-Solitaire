import streamlit as st
from inventory import (
    check_inventory,
    count_item,
    display_inventory,
    end_page,
    is_new_page,
    remove_from_inventory,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=35, book=6)

fr_text = """
Vous prenez votre clé et vous montez à votre chambre, au dernier
étage de l'auberge. Vous ne tardez pas à sombrer dans un profond
sommeil. Vous vous réveillez dès l'aube le lendemain, et l'air
frais du petit matin soufflant par la fenêtre mal ajustée vous
fait frissonner de la tête aux pieds. Tandis que la clarté du jour
naissant inonde la petite mansarde, vous vous apercevez, à votre
grande consternation, que votre Sac à Dos gît à moitié ouvert sur
le plancher. Un trou béant a été pratiqué dans le rabat: l'œuvre
incontestable des rats qui doivent pulluler dans l'établissement !
Tout ce qu'il y avait de comestible dans votre Sac a été dévoré ou
mis en miettes. Rayez toutes vos Provisions sur votre Feuille
d'Aventure avant de quitter l'auberge puis allez chercher votre
cheval.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        st.session_state["visibility_provisions_35"] = count_item("REPAS")
        remove_from_inventory("REPAS", quantity=count_item("REPAS"))
    eaten = st.session_state.get("visibility_provisions_35") or 0
    st.warning(f"Les rats ont dévoré vos Provisions : {eaten} Repas rayé(s) de votre Sac à Dos.")

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_272.py", label="272", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
