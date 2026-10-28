import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=122, book=3)

fr_text = """
Loi-Kymar vous tend quelques lambeaux d'étoffe pour vous
boucher les narines. Vous prenez une profonde inspiration, vous
saisissez le bol d'herbes fumantes et vous quittez la cuisine.
Mettant en pratique la Discipline Kaï du Camouflage, vous vous
fondez parmi les ombres du couloir et vous vous approchez de
plus en plus près des Barbares qui ne se doutent de rien. Vous
posez alors le bol derrière un pilastre et vous retournez dans la
cuisine en attendant que les vapeurs fassent leur effet. Moins
d'une minute plus tard, les Barbares des Glaces tombent
évanouis et vous vous dirigez vers la salle du Trône du
Brumalmarc sans avoir été repéré. A votre grande satisfaction,
vous constatez que l'une des portes incrustées de pierreries n'est
pas fermée à clé. En vous préparant à passer à l'attaque, vous
entrebâillez doucement la porte et vous entrez dans le repaire de
Vonotar.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome3/page_173.py", label="173", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
