import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    pickup_gold,
    show_illustrations,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=331, book=2)

fr_text = """
En fouillant le cadavre du soldat, vous découvrez une Epée, un
Poignard et 3 Pièces d'Or. Puis
soudain, vous entendez le bruit de semelles cloutées qui descendent les
marches de pierre de l'escalier. Vous levez alors la tête et vous
apercevez un autre soldat à l'étage au-dessus. Vous vous précipitez
aussitôt hors de la tour et vous prenez vos jambes à votre cou, tandis
que le soldat vous abreuve d'injures.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write("Vous pouvez garder l'une ou l'autre de ces trouvailles :")
    pickup_button("ÉPÉE", key="epee", label="Prendre l'Épée")
    pickup_button("POIGNARD", key="poignard", label="Prendre le Poignard")
    pickup_gold(3, key="gold")

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_65.py", label="65", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
