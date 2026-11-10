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

check_inventory(current_page_number=91, book=7)

fr_text = """
A votre grande déception, vous constatez que ce tunnel n'est en
réalité qu'un boyau étroit et bas, abritant une couvée d'oeufs gros
comme des barils de bière. Ils reposent sur un lit de déchets et de
vêtements en lambeaux - probablement les dépouilles des
aventuriers précédents, pris au piège du redoutable serpent
géant. Soudain, vous apercevez la mince langue rouge et
fourchue de ce dernier s'immiscer dans le repaire en frétillant.
Vous reculez fébrilement jusqu'au fond de peur de subir un sort
identique à celui de vos malheureux prédécesseurs.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez examiner les œufs de plus près, rendez-vous au :"))
    st.page_link("tomes/tome7/page_148.py", label="148", icon="📄")

    st.write_stream(stream_text("Si vous préférez chercher un moyen de sortir de ce boyau, rendez-vous au :"))
    st.page_link("tomes/tome7/page_346.py", label="346", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
