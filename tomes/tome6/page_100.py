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

check_inventory(current_page_number=100, book=6)

fr_text = """
C'est en fin d'après-midi que vous découvrez enfin Varetta.
Bâtie sur un grand plateau rocheux, la cité s'y dresse depuis
des temps immémoriaux. Ses murs d'enceinte sont immenses,
taillés dans un granit couleur rouge sang, et ses hautes maisons
se tassent les unes contre les autres, s'entremêlant de rue en
rue pour former un dédale compliqué. D'énormes dragons sculptés
dans la pierre serpentent le long des remparts, leur queue
s'enroulant en arabesque autour des portes et des tours de guet.
Des volutes de fumée s'échappent de la gueule des gargouilles
grimaçantes qui se tapissent, tels des espions, au sommet des
tours et des toits. Vous atteignez la porte est de la ville au
coucher du soleil. Le garde en uniforme rouge qui surveille
l'entrée ne fait aucune difficulté pour vous laisser passer, et
vous vous engagez dans les larges avenues de la merveilleuse
cité. Vous arrivez bientôt à un croisement où un poteau en
pierre rouge indique le nom des différentes rues qui en partent.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez aller vers le nord, en prenant l'avenue du Helin, rendez-vous au :"))
    st.page_link("tomes/tome6/page_79.py", label="79", icon="📄")

    st.write_stream(stream_text("Si vous désirez aller vers l'ouest, en passant par l'allée du Coche, rendez-vous au :"))
    st.page_link("tomes/tome6/page_135.py", label="135", icon="📄")

    st.write_stream(stream_text("Si vous préférez vous diriger vers le sud, par la rue de la Flûte, rendez-vous au :"))
    st.page_link("tomes/tome6/page_147.py", label="147", icon="📄")

    st.write_stream(stream_text("Si vous optez pour l'est, continuez la rue où vous vous trouvez et rendez-vous au :"))
    st.page_link("tomes/tome6/page_238.py", label="238", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
