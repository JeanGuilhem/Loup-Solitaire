import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=276, book=6)

fr_text = """
Vous concentrez votre puissance Magnakaï sur le Marteau de Guerre
qui s'élève lentement de la poitrine du cadavre. Vous le faites
venir jusqu'au bord du trou, vous le saisissez par le manche et
l'examinez attentivement. C'est une très belle arme, faite d'un
métal appelé bronin, qui a l'aspect du bronze fraîchement coulé,
mais qui ne se corrode pas comme les alliages ordinaires d'étain
et de cuivre. Si vous souhaitez garder ce Marteau en bronin,
notez-le sur votre Feuille d'Aventure dans la case Armes. Utilisé
au cours d'un combat, il ajoute 1 point à votre total d'HABILETÉ.
Vous vous assurez qu'il n'y a aucun autre objet de valeur, puis
vous quittez la chapelle pour aller rejoindre Cyrilus.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_button("MARTEAU DE GUERRE DE BRONIN", key="t6_276_marteau", label="Prendre le Marteau en bronin")

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_338.py", label="338", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
