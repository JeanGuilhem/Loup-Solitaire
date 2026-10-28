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

check_inventory(current_page_number=174, book=3)

fr_text = """
Le Languabarb est mort, mais l'écho de ses grognements semble
toujours résonner dans la caverne. Soudain, vous voyez une autre
créature semblable surgir du tunnel et foncer sur vous. C'est la
femelle du Languabarb : saisie de rage, elle veut à tout prix
venger son compagnon. Vous n'avez plus à présent qu'un seul
moyen de vous enfuir : traverser le lac.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome3/page_322.py", label="322", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
