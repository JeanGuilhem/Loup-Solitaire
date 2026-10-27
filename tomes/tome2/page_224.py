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

check_inventory(current_page_number=224, book=2)

fr_text = """
Le lendemain matin, vous êtes réveillé par les cris des goélands qui
tournoient au-dessus du clipper. Un fort vent enfle les voiles. Quelques
instants plus tard, vous prenez votre petit déjeuner en compagnie du
capitaine Kelman qui semble plus optimiste que la veille. Il vous
annonce que le Sceptre Vert vogue à bonne allure et que vous devriez
arriver dans une semaine à Port Bax, le port principal du royaume de
Durenor. Puis soudain, un cri retentit dans le nid-de-pie. « Terre par
bâbord avant ! hurle la vigie, terre par bâbord ! » Le capitaine et vous-même
montez alors sur le pont, affrontant la froideur de la brise. « C'est
Mannon, l'île la plus au sud de l'archipel des Kirlundin, dit le capitaine
en montrant une côte rocheuse et accidentée qui se dessine au loin, les
marchands l'appellent la "Pointe des Naufragés" ; nombreux sont les
navires qui ont fini leur carrière sur ces rochers de granit. » Le
capitaine vous tend une lunette d'approche pour vous permettre de
mieux observer l'île. Les rocs pointus de son rivage sont parsemés
d'épaves : ce sont les carcasses fracassées des navires qui s'y sont
échoués ou que la tempête y a précipités. Vous êtes fasciné par le
spectacle de ces coques déchirées et vous imaginez les scènes
terrifiantes qui ont dû se dérouler lors de chacun de ces naufrages. Puis,
brusquement, vous apercevez une ombre noire suspendue au-dessus des
pointes rocheuses de Mannon ; on dirait un petit nuage qui semble se
déplacer dans votre direction. Mais un instant plus tard, vous
comprenez de quoi est fait ce «nuage». Il s'agit en fait d'une nuée de
Bêtalzans auxquels se sont probablement mêlés des Kraans. Aussitôt,
l'alerte est donnée. « Parez au combat ! »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez rester sur le pont, préparez votre arme et rendez-vous au :'))
    st.page_link("tomes/tome2/page_146.py", label="146", icon="📄")

    st.write_stream(stream_text('Si vous préférez retourner dans votre cabine, rendez-vous au :'))
    st.page_link("tomes/tome2/page_34.py", label="34", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
