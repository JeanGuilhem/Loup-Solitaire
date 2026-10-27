import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=140, book=2)

fr_text = """
Les deux gardes contemplent le Sceau avec une stupeur mêlée de
respect. Tous les habitants de Durenor connaissent bien la légende du
Sceau d'Hammardal et l'on dit que, de tous les trésors perdus du
royaume, le Sceau d'Hammardal est celui dont personne ne souhaite le
retour. L'inquiétude qu'exprime le visage des deux gardes montre qu'ils
savent parfaitement ce que l'anneau signifie. L'un des soldats vous
accompagne sur l'autre rive du chenal de Ryner et le long d'une route
forestière qui aboutit à un croisement. Un panneau indicateur orienté
vers l'est précise : PORT BAX 5 km. « Il me faut vous quitter à présent
et retourner au chenal, dit le garde. J'ai bien peur que la guerre ne
vienne bientôt assombrir ce royaume et mon devoir est de surveiller la
frontière. Que Dieu vous accorde son aide, homme du Sommerlund. »
Vous le regardez s'éloigner le long du chemin forestier puis vous vous
remettez en route en direction de l'est. Vous devriez avoir atteint Port
Bax dans une heure tout au plus.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_265.py", label="265", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
