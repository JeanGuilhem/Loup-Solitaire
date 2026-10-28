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

check_inventory(current_page_number=224, book=3)

fr_text = """
A 6 mètres au-dessous environ, vous apercevez un homme vêtu
d'une cape sombre. Il est agenouillé au milieu d'un grand
pentagramme dessiné à la craie sur le sol d'une cellule sale et
obscure.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez appeler cet homme, rendez-vous au :"))
    st.page_link("tomes/tome3/page_67.py", label="67", icon="📄")
    st.write_stream(
        stream_text(
            "Si vous préférez rester silencieux et poursuivre votre chemin le long du couloir en direction de "
            "l'escalier, rendez-vous au :"
        )
    )
    st.page_link("tomes/tome3/page_166.py", label="166", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
