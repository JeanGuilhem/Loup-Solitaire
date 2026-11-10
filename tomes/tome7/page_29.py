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

check_inventory(current_page_number=29, book=7)

fr_text = """
Le souterrain s'enfonce de plus en plus profondément sous le
rocher, puis il débouche subitement sur une pièce baignée d'une
lumière rouge qui jaillit par une ouverture carrée pratiquée dans
le plafond. Tout au bout de la pièce, une grande porte en fer à
deux battants semble être la seule issue. Mais pour y accéder, il
vous faudra passer sous le rideau de lumière rouge...
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez franchir cette étrange zone lumineuse afin d'aller examiner la porte à deux battants, rendez-vous au :"))
    st.page_link("tomes/tome7/page_269.py", label="269", icon="📄")

    st.write_stream(stream_text('Si vous préférez rebrousser chemin pour vous engager ensuite dans le tunnel est, rendez-vous au :'))
    st.page_link("tomes/tome7/page_272.py", label="272", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
