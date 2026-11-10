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

check_inventory(current_page_number=243, book=7)

fr_text = """
Lorsque vous arrivez au milieu du pont, les premiers rats ne sont
plus qu'à quelques mètres de vous. Vous vous retournez pour
leur faire face en tirant une arme, prêt à combattre jusqu'à la
mort si cela se révèle nécessaire. Les rats s'approchent
rapidement et vous passez à l'attaque. Vous les faites tomber du
pont dans le torrent en contrebas mais, au troisième coup, une
secousse fait trembler la pierre. Vous trébuchez, tombez et
atterrissez miraculeusement sur l'autre rive, le souffle coupé,
sain et sauf. Un craquement sonore retentit dans la nuit, et toute
la partie centrale du pont s'effondre dans le ravin dans un
immense éclaboussement. Vous êtes maintenant hors de portée
des rats voraces et vous pouvez continuer à avancer le long de la
plage à une allure moins éprouvante.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_23.py", label="23", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
