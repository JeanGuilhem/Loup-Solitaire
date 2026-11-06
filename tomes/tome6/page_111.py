import streamlit as st
from inventory import (
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

check_inventory(current_page_number=111, book=6)

fr_text = """
Une bourse en velours jaune, accrochée à la ceinture d'un pirate
mort, attire soudain votre attention. Vous la détachez et vous
découvrez qu'elle contient une fiole de Potion de Laumspur, bien
connue pour ses vertus curatives. Il en reste suffisamment pour
vous faire récupérer 4 points d'ENDURANCE. Vous pouvez prendre
ce remède dès maintenant, ou bien le conserver dans votre Sac à
Dos pour plus tard. (N'oubliez pas, dans ce cas, de l'inscrire
sur votre Feuille d'Aventure.)
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_button("POTION DE LAUMSPUR", key="laumspur", label="Prendre la Potion de Laumspur")
    st.caption("Vous pouvez la boire dès maintenant depuis l'onglet Inventaire (4 points d'ENDURANCE).")

    st.write_stream(stream_text("A présent, rendez-vous au :"))
    st.page_link("tomes/tome6/page_77.py", label="77", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
