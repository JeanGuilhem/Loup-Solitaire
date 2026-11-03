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

check_inventory(current_page_number=297, book=4)

fr_text = """
Vers midi, vous êtes forcé de vous arrêter. Vous avez en effet
atteint le sommet d'une colline à partir de laquelle la grand-route
descend peu à peu en direction d'un large pont de bois. C'est le
pont de Ruanon. Vous reconnaissez ses gros piliers noirs et les
eaux sombres de la rivière Xane qui coule au-dessous. De l'autre
côté du pont se dessinent les ruines noircies par le feu d'une
auberge et les silhouettes caractéristiques de brigands à cheval. A
l'entrée du pont, un poteau de signalisation blanc indique : «
Ruanon 20 kilomètres ». Vous êtes conscient qu'il serait
suicidaire d'essayer de franchir le pont. Les brigands disposent
en effet de lourdes arbalètes accrochées à leur selle.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez traverser la rivière en amont, c'est-à-dire vers l'ouest, rendez-vous au :"))
    st.page_link("tomes/tome4/page_113.py", label="113", icon="📄")
    st.write_stream(stream_text("Si vous préférez essayer de traverser cette rivière en aval, c'est-à-dire vers l'est, rendez-vous au :"))
    st.page_link("tomes/tome4/page_252.py", label="252", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
