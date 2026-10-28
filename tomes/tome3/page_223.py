import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=223, book=3)

fr_text = """
Le traîneau contient le matériel détaillé ci-dessous. Vous pouvez
prendre n'importe lequel de ces objets et le ranger dans votre Sac
à Dos, mais n'oubliez pas que vous n'avez pas le droit d'y
transporter plus de huit objets: des provisions équivalentes à 5
Repas (chaque Repas compte pour un objet ; vous pouvez en
emporter autant que vous le désirez, de 1 à 5, dans la limite bien
sûr de la place dont vous disposez) ; une Tente (elle compte pour
3 objets) ; des Couvertures de Fourrure (elles comptent pour 2
objets) ; une Longue Corde (elle compte pour 2 objets). Dyce se
porte volontaire pour retourner avec le traîneau et les chiens à
l'endroit où est ancré le vaisseau Cardonal, tandis que vos deux
autres guides et vous-même poursuivrez votre chemin en
direction d'Ikaya, la Forteresse des Glaces. Ikaya a été taillée
dans la chaîne de Hrod en des temps très anciens, par une race
de créatures qui a depuis longtemps disparu. Des milliers
d'années ont passé avant que les Barbares des Glaces, émigrant
des Étendues Inexplorées, ne viennent s'approprier la forteresse.
Depuis cette époque leurs chefs, que l'on appelle les
«Brumalmarc», exercent leur pouvoir sur les terres de Kalte à
l'abri des murs de glace d'Ikaya. Vous avez parcouru environ 8
kilomètres lorsqu'Irian pointe soudain l'index en direction de
l'ouest. « Là, là-bas, dit-il, j'ai vu quelque chose, j'en suis sûr ! »
Vous vous arrêtez et vous essayez d'apercevoir ce qui a pu lui
apparaître inhabituel dans ce paysage monotone de glace et de
neige. « Regardez là-bas ! » s'écrie alors Fenor, en montrant une
hauteur située à 1,5 kilomètre environ. Vous distinguez alors
deux guerriers vêtus de fourrure qui se tiennent debout sur un
gros bloc de glace. Les deux guerriers vous observent. « Des
Barbares des Glaces, murmure Irian, la voix tremblante de peur.
Si jamais ils arrivent avant nous à Ikaya et signalent notre
présence, autant dire que nous sommes morts. » Vous avez
encore une quinzaine de kilomètres à parcourir pour atteindre la
forteresse et il ne reste que deux heures de jour.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write("Prenez dans le traîneau ce que vous voulez (dans la limite de la place de votre Sac à Dos) :")
    pickup_button("TENTE", key="tente", label="Prendre la Tente (3 places)")
    pickup_button("COUVERTURE DE FOURRURE", key="couverture", label="Prendre les Couvertures de Fourrure (2 places)")
    pickup_button("CORDE", key="corde", label="Prendre la Longue Corde (2 places)")
    for i in range(1, 6):
        pickup_button("REPAS", key=f"repas_{i}", label="Prendre 1 Repas")
    st.write_stream(
        stream_text(
            "Si vous souhaitez ne pas prêter attention à ces Barbares et poursuivre votre chemin vers Ikaya, "
            "rendez-vous au :"
        )
    )
    st.page_link("tomes/tome3/page_327.py", label="327", icon="📄")
    st.write_stream(stream_text("Si vous préférez les attaquer pour essayer de les empêcher de donner l'alerte, rendez-vous au :"))
    st.page_link("tomes/tome3/page_307.py", label="307", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
