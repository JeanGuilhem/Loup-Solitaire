import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    show_illustrations,
    show_map,
)
from text import fr_unknown_magnakai
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=308, book=7)

fr_text = """
A quelque pas devant vous, vous remarquez un carré irrégulier
dans le sol ; signe révélateur de la présence d'un piège. Cela ne
pose aucun problème à un guerrier tel que vous, et vous le
franchissez d'un bond. Un peu plus loin, vous atteignez un
escalier en spirale qui descend vers une caverne aux parois
grossièrement taillées. En bas des marches, un tunnel part vers le
nord et un autre vers l'ouest.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez entrer dans le tunnel nord, rendez-vous au :"))
    st.page_link("tomes/tome7/page_59.py", label="59", icon="📄")
    st.write_stream(stream_text("Si vous préférez entrer dans le tunnel ouest, rendez-vous au :"))
    st.page_link("tomes/tome7/page_323.py", label="323", icon="📄")
    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de Nexus, rendez-vous au :"))
    if has_magnakai("Nexus"):
        st.page_link("tomes/tome7/page_99.py", label="99", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome7/page_99.py", label="99", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
