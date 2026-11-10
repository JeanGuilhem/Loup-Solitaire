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

check_inventory(current_page_number=139, book=7)

fr_text = """
Le sol du tunnel nord est couvert de milliers de petites
empreintes. Des rats, des souris, des vers, des serpents, bref, tous
les hôtes de ces lieux souterrains ont laissé leurs empreintes sur
les dalles poussiéreuses. En revanche, le tunnel est ne comporte
strictement aucune trace ; le sol y est lisse, intact, sans même une
pellicule de poussière. Vous en déduisez aussitôt que ce passage
cache quelque chose...
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez vous engager dans le tunnel est, rendez-vous au :"))
    st.page_link("tomes/tome7/page_101.py", label="101", icon="📄")

    st.write_stream(stream_text("Si vous préférez prendre le tunnel nord, rendez-vous au :"))
    st.page_link("tomes/tome7/page_187.py", label="187", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
