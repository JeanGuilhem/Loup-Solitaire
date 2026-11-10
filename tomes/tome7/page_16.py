import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=16, book=7)

fr_text = """
Il vous faut quelques instants pour vous habituer à la pénombre
qui règne dans cet endroit. Au-dehors, des bruits étranges vous
parviennent de la plage, qui vous poussent à avancer plus
profondément dans ce sombre souterrain, au mépris de toute
prudence. Le sol inégal est couvert de boue, et l'atmosphère
moite et malsaine a des relents de poisson pourri qui vous
soulèvent le cœur. Vous pressez le pas tout en prenant garde de
ne pas glisser, mais, bientôt, l'obscurité devient si dense que vous
devez faire halte.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    light = has_item("SPHÈRE DE FEU") or has_item("LANTERNE") or has_item("TORCHE") or has_item("BRIQUET À AMADOU")
    st.write_stream(stream_text("Si vous possédez une Sphère de Feu de Kalte, une Lanterne, une Torche ou un Briquet d'Amadou, rendez-vous au :"))
    st.page_link("tomes/tome7/page_61.py", label="61", icon="📄", disabled=not light)

    st.write_stream(stream_text('Si vous ne possédez aucun de ces objets, rendez-vous au :'))
    st.page_link("tomes/tome7/page_277.py", label="277", icon="📄", disabled=light)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
