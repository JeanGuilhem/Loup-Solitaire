import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=333, book=2)

fr_text = """
Le marin qui se faisait passer pour Ronan semble avoir pris la fuite au
cours du combat. Vous fouillez rapidement les cadavres des autres
brigands, mais vous ne découvrez rien d'intéressant. Vous remarquez
cependant que chacun des malfaiteurs porte au poignet gauche un
tatouage représentant un serpent. Il est clair que celui qui leur a donné
l'ordre de vous tuer, quel qu'il soit, connaît déjà la nature de votre
mission. Vous quittez la taverne par la porte latérale et vous découvrez
en passant devant un escalier le cadavre d'un marin dissimulé sous les
marches. Cousue à l'intérieur du col de sa veste tachée de sang, une
étiquette porte ce nom : Ronan. Voilà donc celui avec qui vous aviez
rendez-vous et que vos ennemis ont assassiné pour prendre sa place.
Vous couvrez son corps et vous sortez de la taverne en prenant la
direction du port dans lequel est ancré le Sceptre Vert, à quelque 300
mètres du quai.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez rejoindre le navire en empruntant l'un des canots qui sont amarrés le long du quai, rendez-vous au :"))
    st.page_link("tomes/tome2/page_300.py", label="300", icon="📄")
    st.write_stream(stream_text("Si vous préférez essayer de retrouver l'imposteur qui s'est fait passer pour Ronan, rendez-vous au :"))
    st.page_link("tomes/tome2/page_67.py", label="67", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
