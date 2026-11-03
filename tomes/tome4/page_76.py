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

check_inventory(current_page_number=76, book=4)

fr_text = """
Les Gardes refusent de répondre à vos questions. Le châtiment
que leur ferait subir leur chef s'ils le trahissaient semble leur faire
beaucoup plus peur que d'éventuelles tortures infligées par vos
hommes. Tout ce que vous pouvez conclure en observant leurs
uniformes et leur comportement, c'est qu'ils appartiennent à la
même horde de brigands que celle qui vous a attaqué
auparavant.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez les fouiller, rendez-vous au :"))
    st.page_link("tomes/tome4/page_268.py", label="268", icon="📄")

    st.write_stream(stream_text("Si vous préférez quitter les lieux, rendez-vous au :"))
    st.page_link("tomes/tome4/page_64.py", label="64", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
