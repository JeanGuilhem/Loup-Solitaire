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

check_inventory(current_page_number=150, book=4)

fr_text = """
Le sentier mène à l'entrée d'une galerie de mine à moitié
masquée par des feuillages. Vous jetez un coup d'oeil dans ce
passage obscur et vous constatez que plusieurs poutres et étais se
sont effondrés. Des monticules de terre couverts de mousse
parsèment le sol du tunnel et une rigole d'eau teintée par le
minerai serpente parmi eux. Les traces de sabots s'interrompent
devant l'entrée, mais deux rangées d'empreintes de pas
s'enfoncent à l'intérieur de la mine.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez envoyer vos hommes à la recherche des chevaux disparus, rendez-vous au :'))
    st.page_link("tomes/tome4/page_164.py", label="164", icon="📄")

    st.write_stream(stream_text("Si vous préférez suivre les traces de pas à l'intérieur de la galerie, rendez-vous au :"))
    st.page_link("tomes/tome4/page_288.py", label="288", icon="📄")

    st.write_stream(stream_text('Enfin, si vous préférez interrompre les recherches, vous pouvez revenir sur vos pas le long du sentier de la colline en vous rendant au :'))
    st.page_link("tomes/tome4/page_6.py", label="6", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
