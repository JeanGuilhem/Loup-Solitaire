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

check_inventory(current_page_number=347, book=3)

fr_text = """
Le couloir n'est que faiblement éclairé et votre grande habileté de
chasseur doit vous permettre de vous approcher des gardes en
vous glissant dans l'ombre sans être vu. Vous protégeant le nez
des vapeurs qui s'élèvent du bol, vous avancez pas à pas le long
du mur sans que les Barbares soupçonnent votre présence. Vous
posez ensuite le bol à l'ombre d'un pilastre et vous retournez sans
bruit vers la cuisine, attendant que les herbes produisent leur
effet. Moins d'une minute plus tard, les Barbares des Glaces
s'effondrent sur le sol. La voie est libre et vous pouvez vous
diriger vers la salle du Trône du Brumalmarc en toute sécurité.
Vous êtes alors ravi de constater que l'une des grandes portes
incrustées de pierreries n'est pas fermée à clé. Vous tenant prêt à
combattre, vous l'entrebâillez doucement et vous pénétrez dans
le repaire de Vonotar.
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
