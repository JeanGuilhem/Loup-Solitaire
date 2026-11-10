import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    pickup_button,
    show_illustrations,
    show_map,
)
from text import fr_unknown_magnakai
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=236, book=7)

fr_text = """
Les marches mènent à une pièce ordinaire aux murs en pierre,
sans meubles, excepté un râtelier accroché au mur du fond. Vous
y trouvez une lance et une épée, toutes deux en très bon état.
Deux tunnels éclairés par des torches partent de la pièce : l'un
vers le nord, l'autre vers l'est.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_button("LANCE", key="lance")
    pickup_button("ÉPÉE", key="epee")

    st.write_stream(stream_text("Si vous souhaitez suivre le tunnel nord, rendez-vous au :"))
    st.page_link("tomes/tome7/page_187.py", label="187", icon="📄")

    st.write_stream(stream_text("Si vous préférez suivre le tunnel est, rendez-vous au :"))
    st.page_link("tomes/tome7/page_101.py", label="101", icon="📄")

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de l'Exploration, rendez-vous au :"))
    if has_magnakai("Exploration"):
        st.page_link("tomes/tome7/page_139.py", label="139", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome7/page_139.py", label="139", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
