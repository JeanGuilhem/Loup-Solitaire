import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    item_info,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=298, book=7)

fr_text = """
Après une centaine de mètres, le passage tourne brusquement à
droite. Brillant dans la faible lumière, vous apercevez devant
vous un amas de bulles géantes, flottant lentement à mi-hauteur
dans le tunnel. Mues par une brise légère, les bulles avancent
dans votre direction.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez avancer au milieu des bulles pour continuer le long du tunnel, rendez-vous au :"))
    st.page_link("tomes/tome7/page_107.py", label="107", icon="📄")

    sword = any(
        item_info(item).get("mastery") == "ÉPÉE" for item in st.session_state.weapons + st.session_state.special
    )
    st.write_stream(stream_text("Si vous possédez une épée et que vous voulez percer les bulles, rendez-vous au :"))
    st.page_link("tomes/tome7/page_151.py", label="151", icon="📄", disabled=not (sword))

    st.write_stream(stream_text("Si vous préférez retourner dans la pièce et prendre le tunnel de droite, rendez-vous au :"))
    st.page_link("tomes/tome7/page_322.py", label="322", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
