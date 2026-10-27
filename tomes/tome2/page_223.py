import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=223, book=2)

fr_text = """
Le garde contemple avec une stupeur mêlée de respect le magnifique
anneau que vous lui montrez. Les habitants de Durenor connaissent
bien la légende du Sceau d'Hammardal et l'on dit que de tous les trésors
perdus du royaume, le Sceau est celui dont personne ne souhaite le
retour. Le visage inquiet du soldat montre qu'il sait parfaitement ce que
signifie le retour du Sceau d'Hammardal : c'est la guerre qu'il annonce.
« Je ne peux malheureusement rien faire pour vous aider, dit le garde, si
ce n'est vous indiquer la route pour Port Bax. Suivez ce chemin
forestier et vous arriverez à une bifurcation, à proximité d'un petit
chêne. Prenez alors le sentier de gauche, c'est un raccourci. » Vous
remerciez ce loyal soldat et vous repartez dans la forêt. Deux
kilomètres plus loin environ, vous arrivez à la bifurcation et vous
prenez le sentier de gauche. Il vous amène à un pont de pierre qui
traverse le chenal de Ryner. Les eaux du chenal font plus de 1500 m de
profondeur et plus de 3 kilomètres dans leur plus grande largeur. Près
du pont un poteau indicateur précise : PORT BAX 5 km. Vous poussez
un soupir de soulagement car dans moins d'une heure, vous devriez être
rendu.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome2/page_265.py", label="265", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
