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

check_inventory(current_page_number=296, book=5)

fr_text = """
A l'intérieur, l'auberge est pleine d'autochtones assis à de petites
tables de pierre. Des narguilés finement ouvragés ajoutent à
l'atmosphère colorée des lieux, tandis que les fumeurs discutent
à bâtons rompus de toutes sortes de sujets. Un trio bruyant se
lamente de la mort du vieux Zakhan, tandis que d'autres font des
reproches au nouveau souverain, le traitant de bœuf, de brute, et
autres qualificatifs peu flatteurs. A votre avis, ils expriment trop
fort leurs opinions... Deux Ikareshis à la mine sévère vous font
un signe de bienvenue puis vous invitent à partager leurs pipes.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez accepter leur offre, rendez-vous au :"))
    st.page_link("tomes/tome5/page_362.py", label="362", icon="📄")

    st.write_stream(stream_text("Si vous préférez la décliner, vous pouvez quitter l'auberge et continuer à remonter l'avenue. Rendez-vous au :"))
    st.page_link("tomes/tome5/page_388.py", label="388", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
