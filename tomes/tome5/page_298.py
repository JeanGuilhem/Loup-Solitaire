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

check_inventory(current_page_number=298, book=5)

fr_text = """
Vous vous demandez si vous devez forcer la porte, lorsque vous
entendez soudain les pierres frotter lentement l'une contre
l'autre. La porte coulisse lentement et vous pénétrez dans une
grande pièce faiblement éclairée. Derrière vous, la porte se
referme à une vitesse déconcertante ! Malgré l'obscurité, vous
distinguez de nombreuses empreintes de pas dans l'épaisse
couche de poussière qui recouvre le sol de marbre. Vous
remarquez en entrant qu'un trône en pierre se dresse au centre
de la pièce, face au mur du fond.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_289.py", label="289", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
