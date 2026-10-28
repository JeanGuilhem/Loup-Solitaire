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

check_inventory(current_page_number=120, book=3)

fr_text = """
Le cyclone souffle avec tant de rage qu'il en déchire presque vos
vêtements en vous bombardant sans cesse d'éclats de pierre ou
de glace, pointus comme des aiguilles. Lorsque vous levez le
Glaive de Sommer, un mugissement sonore retentit à vos
oreilles. C'est un hurlement d'horreur et de désespoir. Vous
portez alors un coup de votre arme redoutable, fendant le
tourbillon, transperçant la substance impalpable du Démon. Un
instant plus tard, le cyclone a disparu et les effroyables
gémissements se sont tus. Il ne reste plus, éparpillés sur le sol,
que les débris fracassés d'une statue creuse.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez examiner l'autel, rendez-vous au :"))
    st.page_link("tomes/tome3/page_274.py", label="274", icon="📄")
    st.write_stream(stream_text("Si vous préférez quitter le temple, vous pouvez partir en franchissant l'arcade située au nord. Rendez-vous pour cela au :"))
    st.page_link("tomes/tome3/page_306.py", label="306", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
