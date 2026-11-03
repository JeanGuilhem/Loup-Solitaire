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

check_inventory(current_page_number=79, book=4)

fr_text = """
Vous parvenez tant bien que mal à vous relever et vous avancez
d'un pas chancelant le long du sentier forestier qui monte vers
les contreforts de la chaîne de Maaken. Soudain, le sentier
s'arrête à l'entrée d'une galerie de mines à moitié dissimulée par
des feuillages. Il s'agit là sans aucun doute d'un tunnel désaffecté
qui donne accès aux mines de Maaken dont le réseau souterrain
sillonne les profondeurs des montagnes de la région. Si vous
parvenez à découvrir l'un des principaux puits de la mine, vous
devriez pouvoir atteindre Ruanon en passant par ces galeries
souterraines. Dès que vous avez pénétré dans le tunnel, vous
trouvez une caisse brisée qui contient 5 Torches et 1 Briquet
d'Amadou. Il règne une totale obscurité dans cette galerie et vous
aurez besoin d'au moins 1 Torche pour vous éclairer. Vous
pouvez cependant prendre autant de Torches que vous le
souhaiterez, chacune d'elles comptant pour un objet dans votre
Sac à Dos. Le tunnel est glacial et peu accueillant. Vous le
parcourez pendant plus d'un kilomètre et demi avant d'arriver à
un croisement. Là, un autre tunnel bifurque en direction du sud.
Il semble avoir été creusé plus récemment et vous l'empruntez
dans l'espoir de découvrir l'un des puits principaux de la mine.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write("Vous pouvez prendre autant de Torches que vous le souhaitez, ainsi que le Briquet d'Amadou :")
    for number in range(1, 6):
        pickup_button("TORCHE", key=f"torche_{number}", label=f"Prendre une Torche ({number}/5)")
    pickup_button("BRIQUET À AMADOU", key="briquet", label="Prendre le Briquet d'Amadou")

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome4/page_117.py", label="117", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
