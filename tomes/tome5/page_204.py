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

check_inventory(current_page_number=204, book=5)

fr_text = """
Vous sentez que la pierre émet des radiations extrêmement
dangereuses et maléfiques. Si vous pouviez seulement retourner
le pouvoir de cette pierre contre le Seigneur des Ténèbres, celui-ci serait dépossédé de sa force. Bien que la pierre ne puisse pas
tuer Haakon, elle pourrait au moins l'exiler en un lieu où il ne
pourrait plus rien faire pour vous nuire.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez essayer de vous emparer de la pierre pour la tourner contre votre ennemi, rendez-vous au :"))
    st.page_link("tomes/tome5/page_268.py", label="268", icon="📄")

    st.write_stream(stream_text("Si vous préférez laisser la pierre et attaquer le Seigneur des Ténèbres avec votre arme, rendez-vous au :"))
    st.page_link("tomes/tome5/page_390.py", label="390", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
