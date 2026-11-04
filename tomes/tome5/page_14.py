import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    overloaded,
    restore_confiscated,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=14, book=5)

fr_text = """
Vous pénétrez dans une pièce parfaitement hémisphérique dont
les murs s'incurvent progressivement jusqu'au plafond, où une
lucarne déverse sur le sol un flot de lumière. Il y a une énorme
table circulaire au centre de la pièce, sur laquelle sont disposés
des brûle-parfums, des carafes, des plumes, des rouleaux de
parchemin, de grandes capes, des urnes et toutes sortes de fruits
et de sucreries. Un grand tiroir légèrement entrouvert attire
votre attention, et vous découvrez son contenu en l'ouvrant: il
s'agit de l'équipement que l'on vous a confisqué ! Inscrivez à
nouveau sur votre Feuille d'Aventure tous les objets que
contenait votre Sac à Dos, sans oublier les Objets Spéciaux, les
armes et les Pièces d'Or que vous aviez perdus lors de votre
emprisonnement. Rempli de joie et de confiance par votre
découverte, vous décidez de vous enfuir le plus vite possible du
Grand Palais. Exception faite de la porte par laquelle vous êtes
entré, il n'y a qu'une autre issue - située au nord - à la pièce où
vous vous trouvez.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        if restore_confiscated():
            st.success("Vous récupérez votre Sac à Dos, vos armes, vos Objets Spéciaux et vos Pièces d'Or.")

    # l'équipement retrouvé s'ajoute à celui ramassé entre-temps : il faut d'abord faire de la place
    blocked = overloaded()
    if blocked:
        st.warning("Vous portez trop d'objets : jetez-en depuis l'onglet Inventaire avant de repartir.")

    st.write_stream(stream_text('Si vous désirez à présent quitter cet endroit, rendez-vous au :'))
    st.page_link("tomes/tome5/page_58.py", label="58", icon="📄", disabled=blocked)
    st.write_stream(stream_text('Si vous préférez auparavant fouiller la pièce afin de découvrir des objets utiles, rendez-vous au :'))
    st.page_link("tomes/tome5/page_131.py", label="131", icon="📄", disabled=blocked)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
