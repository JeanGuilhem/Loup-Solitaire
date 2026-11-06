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

check_inventory(current_page_number=125, book=6)

fr_text = """
La bière coule à flots et les soldats se racontent leurs
exploits guerriers avec une exagération démesurée. Ils sont
bruyants et agités, mais un silence gênant tombe subitement à
votre approche. Vous remarquez que leurs mains ont prestement
abandonné leurs chopes de bière pour se poser fermement sur la
garde des lourdes épées qui pendent à leur côté.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez offrir un verre à ces hommes d'armes méfiants, rendez-vous au :"))
    st.page_link("tomes/tome6/page_30.py", label="30", icon="📄")

    st.write_stream(stream_text("Si vous préférez leur demander la permission de vous asseoir à leur table, rendez-vous au :"))
    st.page_link("tomes/tome6/page_260.py", label="260", icon="📄")

    st.write_stream(stream_text("Si vous jugez plus sage de les éviter et d'aller vous installer à une autre table pour commander un repas, rendez-vous au :"))
    st.page_link("tomes/tome6/page_172.py", label="172", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
