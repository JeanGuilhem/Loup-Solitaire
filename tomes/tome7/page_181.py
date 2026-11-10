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

check_inventory(current_page_number=181, book=7)

fr_text = """
La patrouille fait halte à moins de trois mètres de l'endroit où
vous êtes caché. Le chef aboie un ordre, et l'un des gardes revêtus
d'une armure noire sort un briquet de sa poche, puis allume une
torche en goudron fixée au mur. La torche s'embrase en
grésillant, et vous êtes pris dans la vive lumière de la flamme
jaune.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez un arc et que vous souhaitez tirer sur les gardes avant qu'ils ne remarquent votre présence, rendez-vous au :"))
    st.page_link("tomes/tome7/page_206.py", label="206", icon="📄", disabled=not can_shoot())

    st.write_stream(stream_text("Si vous voulez attaquer les gardes avec une autre arme, rendez-vous au :"))
    st.page_link("tomes/tome7/page_332.py", label="332", icon="📄")

    st.write_stream(stream_text("Si vous préférez traverser la pièce en courant pour essayer de fuir par le couloir du fond, rendez-vous au :"))
    st.page_link("tomes/tome7/page_69.py", label="69", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
