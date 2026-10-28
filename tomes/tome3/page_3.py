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

check_inventory(current_page_number=3, book=3)

fr_text = """
Vous regardez les morceaux fracassés de la créature se dissoudre
dans la glace avec un mélange de répulsion et de fascination.
Bientôt, il ne reste plus du Serpent de Cristal que les reliefs de
nourriture qui n'avaient pas encore été digérés par son estomac.
A votre grand étonnement, vous apercevez, dans cette bouillie
fétide de chair et d'os, la tige d'une Clé d'Argent.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez prendre cette Clé, rendez-vous au :'))
    st.page_link("tomes/tome3/page_280.py", label="280", icon="📄")

    st.write_stream(
        stream_text(
            "Si vous préférez ne pas y faire attention et essayer de trouver le moyen d'ouvrir la "
            'porte de la forteresse, rendez-vous au :'
        )
    )
    st.page_link("tomes/tome3/page_344.py", label="344", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
