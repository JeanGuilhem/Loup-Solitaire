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

check_inventory(current_page_number=213, book=6)

fr_text = """
Vous suivez l'homme dans un couloir fermé par des rideaux
jusqu'à une pièce au haut plafond voûté. Une odeur âcre et
nauséabonde de cadavre et de formol emplit l'atmosphère.
D'étranges carcasses d'animaux pendent à des crochets fixés au
plafond et des têtes disséquées, sortes de trophées de chasse,
reposent sur de grands établis. L'homme ouvre un coffret en bois
de rose ouvragé et en retire un plateau d'argent sur lequel il pose
deux verres en cristal et une carafe de vin couleur vermeil. Il
remplit ensuite les verres puis il vous en offre un, en vous
précisant que le vin vous aidera à oublier l'odeur désagréable de
l'atelier.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez accepter son offre gracieuse, prenez le verre qui vous est destiné et rendez-vous au :"))
    st.page_link("tomes/tome6/page_288.py", label="288", icon="📄")

    st.write_stream(stream_text("Si vous préférez décliner son offre, quittez l'atelier d'empaillage et rendez-vous au :"))
    st.page_link("tomes/tome6/page_279.py", label="279", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
