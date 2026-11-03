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

check_inventory(current_page_number=115, book=4)

fr_text = """
Tandis que le bateau franchit l'arcade aménagée dans le mur
situé au sud, vous ramenez votre cape de Seigneur Kaï autour de
vos épaules en relevant le capuchon. Vous venez en effet de
pénétrer dans un tunnel dont le plafond laisse échapper des
gouttes d'eau couleur de rouille qui tachent les cheveux et les
tuniques de vos hommes. Vous ramez pendant un kilomètre et
demi environ avant d'arriver dans une petite caverne. Un escalier
émergeant de la rivière mène à une autre arcade s'ouvrant dans
la paroi rocheuse.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez aborder au pied de cet escalier pour explorer le tunnel au-delà de l'arcade, rendez-vous au :"))
    st.page_link("tomes/tome4/page_8.py", label="8", icon="📄")

    st.write_stream(stream_text('Si vous préférez continuer à descendre la rivière en direction du sud, rendez-vous au :'))
    st.page_link("tomes/tome4/page_240.py", label="240", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
