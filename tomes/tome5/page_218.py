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

check_inventory(current_page_number=218, book=5)

fr_text = """
Les Nains poursuivent leur repas, s'arrêtant uniquement de
temps en temps pour allumer de grandes pipes à couvercle. A
travers les volutes de fumée bleue qui s'élèvent dans la petite
cabine, vous remarquez qu'ils vous jettent des regards inquiets,
comme si vous alliez vous écrouler d'un instant à l'autre. Au bout
de cinq minutes, Nolrim lève sa chope pour porter un toast : « A
Loup Solitaire, un homme parmi les Nains ! » Les Nains rient
grassement aux paroles ironiques de Nolrim, puis à leur tour ils
lèvent leurs chopes pour saluer votre courage et votre vaillance.
La bière de Bor a délié leur langue et ils sont tous impatients de
vous raconter leurs anciens faits d'armes.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_291.py", label="291", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
