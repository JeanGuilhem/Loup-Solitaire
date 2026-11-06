import streamlit as st
from inventory import (
    buy_button,
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

check_inventory(current_page_number=123, book=6)

fr_text = """
Une poignée de Baies d'Alether coûte 3 Pièces d'Or. Si vous en
mangez avant le combat, cela vous permettra d'ajouter 2 points à
votre total d'HABILETÉ pour toute la durée de l'affrontement.
Vous pouvez acheter au maximum 3 poignées de Baies d'Alether (à
condition, bien sûr, d'en avoir les moyens !). Chaque poignée
compte pour 1 Objet de votre Sac à Dos. Par ailleurs,
souvenez-vous que vous ne pouvez avaler qu'une seule poignée
avant d'entreprendre un combat. Une fois vos achats terminés,
remontez en selle et quittez le village.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    for index in range(1, 4):
        buy_button("BAIES D'ALETHER", 3, key=f"baies_{index}", label=f"Acheter une poignée de Baies d'Alether (3 Pièces d'Or) — {index}/3")

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_100.py", label="100", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
