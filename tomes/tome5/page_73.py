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

check_inventory(current_page_number=73, book=5)

fr_text = """
La puanteur de l'égout se dissipe peu à peu et l'eau s'éclaircit au
fur et à mesure que vous avancez. Les bruits de pas des hommes
de Maouk se sont évanouis au loin et vous n'entendez plus à
présent que le clapotis des eaux sales. Soudain, votre pied heurte
quelque chose et vous perdez l'équilibre. Vous découvrez, à demi
enlisée dans le sol vaseux, une vieille armure rouillée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_94.py", label="94", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
