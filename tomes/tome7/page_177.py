import streamlit as st
from inventory import (
    can_shoot,
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

check_inventory(current_page_number=177, book=7)

fr_text = """
Le soulagement est immédiat. Rapidement, vous sautez d'une
pierre à l'autre. A l'instant même où vous atteignez l'ouverture
pratiquée dans le mur, un bruissement se fait entendre dans
l'obscurité et, soudain, un objet rond et noir jaillit du lac dans un
atroce hurlement. La sphère flotte un instant au-dessus de l'eau,
puis file vers vous à la vitesse de l'éclair.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Vous pouvez tenter de vous glisser dans la fissure, rendez-vous au :"))
    st.page_link("tomes/tome7/page_16.py", label="16", icon="📄")

    st.write_stream(stream_text("Vous pouvez également tirer une arme pour affronter cette étrange sphère, rendez-vous au :"))
    st.page_link("tomes/tome7/page_342.py", label="342", icon="📄")

    st.write_stream(stream_text("Enfin, si vous possédez un arc et que vous souhaitiez l'utiliser, rendez-vous au :"))
    st.page_link("tomes/tome7/page_225.py", label="225", icon="📄", disabled=not can_shoot())

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
