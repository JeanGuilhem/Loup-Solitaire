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

check_inventory(current_page_number=69, book=4)

fr_text = """
Vous enjambez le cadavre du Garde et vous constatez alors que la
corde qui pend du plafond est reliée à des broches de fixation
grâce auxquelles le pont reste attaché au bord du puits. Si le
Garde avait tiré sur la corde, la passerelle se serait
immédiatement décrochée et vous auriez été bloqué de ce côté de
la salle. Vous vous hâtez de franchir le pont au moment où vos
poursuivants font leur apparition. De l'autre côté de la passerelle,
vous trouvez une corde semblable également pendue au plafond,
à côté de l'entrée du tunnel aménagée dans le mur ouest. Vos
poursuivants sont à présent au beau milieu du pont.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez tirer sur la corde, rendez-vous au :"))
    st.page_link("tomes/tome4/page_125.py", label="125", icon="📄")

    st.write_stream(stream_text("Si vous préférez vous en abstenir et vous enfuir dans le tunnel, rendez-vous au :"))
    st.page_link("tomes/tome4/page_348.py", label="348", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
