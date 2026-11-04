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

check_inventory(current_page_number=318, book=5)

fr_text = """
« Ah ! Tipasa... réplique-t-il pensivement, il ne demeure pas loin
du marché aux Douggas, mais je ne sais pas où exactement. De
plus, cela fait des années que je n'ai vu le vieux Tipasa. Si
toutefois vous le trouvez, rappelez-le au bon souvenir de
Khamsin le chevrier ; il me doit toujours 20 Pièces d'Or et moi, je
ne l'ai pas oublié ! » Après avoir remercié le vieux chevrier, vous
prenez congé de lui et vous vous remettez en route pour Ikaresh.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome5/page_272.py", label="272", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
