import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=190, book=6)

fr_text = """
Fou de haine et de rage, le Yamsark saute droit sur vous du haut
de l'amas de décombres. Mais, aveuglé par sa fureur, il ne voit
pas le précipice qui s'ouvre derrière vous. Vous faites un saut de
côté, et il tombe dans le vide la tête la première. Quelques
secondes plus tard, vous entendez un cri strident : la créature
vient de s'écraser sur les rochers, trente mètres plus bas. Choqué,
mais satisfait de vous en être sorti sain et sauf, vous retournez
vers la chapelle et vous remplissez votre flacon en verre d'Eau de
Taunor (l'eau minérale contenue dans le flacon peut faire
regagner 6 points d'ENDURANCE). Vous pouvez boire l'Eau
maintenant ou bien la garder dans votre Sac à Dos pour plus
tard.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # l'Eau de Taunor : à boire tout de suite (+6) ou à garder dans le Sac à Dos (un seul des deux)
    if not st.session_state.get("visibility_eau_taunor"):
        if st.button("Boire l'Eau de Taunor maintenant (+6 ENDURANCE)", key="drink_taunor"):
            st.session_state["visibility_eau_taunor"] = True
            change_endurance(6)
            st.rerun()
    pickup_button("EAU DE TAUNOR", key="eau_taunor", label="Garder l'Eau de Taunor dans le Sac à Dos")

    st.write_stream(stream_text("Si vous souhaitez examiner la chapelle, rendez-vous au :"))
    st.page_link("tomes/tome6/page_24.py", label="24", icon="📄")

    st.write_stream(stream_text("Si vous préférez rejoindre Cyrilus, rendez-vous au :"))
    st.page_link("tomes/tome6/page_338.py", label="338", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
