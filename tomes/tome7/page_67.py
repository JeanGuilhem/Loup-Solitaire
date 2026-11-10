import streamlit as st
from inventory import (
    can_shoot,
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

check_inventory(current_page_number=67, book=7)

fr_text = """
La flèche fend l'air en sifflant et atteint la créature de tête en
plein front. Votre victime s'arrête net, comme figée sur place, et
un curieux grésillement s'échappe de ses mâchoires béantes.
Puis, elle prend subitement feu. En l'espace de quelques
secondes, son corps se consume et se désagrège en une substance
incandescente et poisseuse comme de la lave en fusion.
Apparemment peu affectées par le sort de leur congénère, les
autres créatures canines accélèrent leur démarche louvoyante et,
dans un déclic crissant, de longues griffes recourbées jaillissent
de leurs doigts palmés.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez tirer une autre flèche, rendez-vous au :"))
    st.page_link("tomes/tome7/page_175.py", label="175", icon="📄", disabled=not (can_shoot()))

    st.write_stream(stream_text("Si vous préférez ranger rapidement votre arc et prendre la fuite par le passage voûté qui se trouve à l'opposé, rendez-vous au :"))
    st.page_link("tomes/tome7/page_241.py", label="241", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
