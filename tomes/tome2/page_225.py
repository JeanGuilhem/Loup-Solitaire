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

check_inventory(current_page_number=225, book=2)

fr_text = """
Soixante-dix navires de guerre de la flotte de Durenor avaient quitté
Port Bax mais ils ne sont plus que cinquante à entrer dans le golfe de
Holm. La bataille a coûté la vie à nombre de vaillants soldats, parmi
lesquels l'amiral Calfen en personne qui fut tué à bord du Durenor, le
premier navire à avoir sombré au cours des combats. Mais en dépit des
lourdes pertes, une grande victoire a été remportée, une victoire qui a
donné aux soldats une vigueur nouvelle. La double épreuve du voyage
et de la bataille a été oubliée à présent ; la même détermination, le
même optimisme qu'ils avaient manifestés à leur départ de Port Bax les
animent à nouveau et tous ont hâte de gagner Holmgard pour défaire
l'ennemi. Au 37e jour de votre quête, à la tombée de la nuit, les tours de
Holmgard apparaissent enfin à l'horizon. La ville continue de résister à
l'armée des Maîtres des Ténèbres bien que le siège ait été constamment
maintenu. Les lumières de la capitale luisent dans l'obscurité tandis
que, debout à la proue du navire, vous contemplez les rivages du
royaume. Un Lord Axim confiant dans l'issue de la bataille vient vous
rejoindre. « Cette nuit sans lune va nous avantager, assure-t-il, l'ennemi
ne nous verra pas entrer dans le port et, dès l'aube, mes hommes
balaieront ces misérables comme des feuilles mortes emportées par le
vent. » Et lorsque votre navire entre dans le port de Holmgard, à la tête
de la flotte de Durenor, vous tirez de son fourreau le Glaive de
Sommer, prêt à accomplir votre destinée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome2/page_350.py", label="350", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
