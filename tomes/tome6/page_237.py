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

check_inventory(current_page_number=237, book=6)

fr_text = """
La foule s'est rassemblée pour assister au combat. Au moment où
vous portez le coup de grâce, une clameur s'élève de l'assistance.
Mais, aussitôt, vous êtes bousculé violemment et ils se jettent sur
le corps de Barbenoire comme des vautours : la meute avide
dépouille le mort de tous ses biens. Indigné par leur
comportement, vous faites demi-tour et vous partez au galop loin
de ce spectacle dégradant.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_279.py", label="279", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
