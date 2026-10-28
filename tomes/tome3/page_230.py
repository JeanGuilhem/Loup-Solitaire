import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=230, book=3)

fr_text = """
Le Monstre d'Enfer se consume et se décompose à vos pieds, un
gaz vert et nauséabond s'échappant de ses vêtements. Tandis que
vous contemplez avec horreur sa répugnante dépouille, vous
songez que cette créature a dû être envoyée ici pour tuer Vonotar ;
les Maîtres des Ténèbres, en effet, voulaient ainsi faire payer au
mage félon sa défaite dans la bataille du golfe de Holm. Vonotar
a sans doute découvert la présence du Monstre d'Enfer dans la
forteresse et l'a emprisonné dans un pentagramme en attendant
de trouver le moyen de s'en débarrasser définitivement. Vous
tâtez avec précaution votre gorge blessée en remerciant les dieux
d'avoir pu brandir le Glaive de Sommer : son pouvoir, une fois de
plus, vous a sauvé la vie. Enfin, vous abandonnez les restes
nauséabonds du Monstre d'Enfer, et vous vous hâtez de
descendre l'escalier.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome3/page_166.py", label="166", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
