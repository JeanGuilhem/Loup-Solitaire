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

check_inventory(current_page_number=161, book=7)

fr_text = """
Alors que les derniers survivants s'enfuient à tire-d'aile au plus
profond des ténèbres, vous rengainez votre arme et vous
repoussez du pied les cadavres des vampires tombés sous vos
coups. En bas de l'escalier, vous débouchez sur une pièce vide et
nue, à l'exception d'un râtelier accroché au mur du fond. Il
contient une Lance et un Glaive, tous deux en parfait état. Vous
pouvez sortir de cette pièce par deux tunnels éclairés par des
torches ; l'un descend vers le nord, l'autre vers l'est.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_button("LANCE", key="lance_161", label="Prendre la Lance")
    pickup_button("GLAIVE", key="glaive_161", label="Prendre le Glaive")

    st.write_stream(stream_text("Si vous voulez vous engager dans le tunnel nord, rendez-vous au :"))
    st.page_link("tomes/tome7/page_187.py", label="187", icon="📄")

    st.write_stream(stream_text("Si vous préférez prendre le tunnel est, rendez-vous au :"))
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
