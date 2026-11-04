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

check_inventory(current_page_number=67, book=5)

fr_text = """
Vous percevez un faible déclic suivi d'un léger tremblement
lorsque la porte s'ouvre en tournant lentement sur ses gonds.
Vous vous engagez rapidement dans l'ouverture, et la porte se
referme aussitôt sur vous, aussi doucement qu'elle s'était
ouverte. D'instinct, vous réalisez que vous êtes à présent dans la
partie supérieure du Palais, où sont installés les luxueux
appartements privés du Zakhan. Le sol de la pièce que vous
traversez est incrusté de fines plaques d'opale et de platine
étincelantes. Vous passez devant une précieuse collection de
statues en or massif, et la porte en améthyste qui se trouve en
face de vous semble ordinaire à côté des merveilles éblouissantes
de ce monde secret. Cette porte s'ouvre sur un autre endroit, tout
aussi fascinant que le précédent: l'Arboretum. Il s'agit d'un
espace parfaitement circulaire dont la voûte, semblable à celle
d'une cathédrale, paraît tapissée de velours vert. De la terre
sombre qui recouvre le sol s'élèvent des arbres de toutes
couleurs, de toutes tailles et de formes variées. Cette voûte
végétale est tout entière emplie de chants d'oiseaux. Les serres
du Zakhan renferment un spécimen de chaque arbre poussant
dans le Magnamund, ainsi que certaines espèces totalement
disparues à l'heure actuelle. Tandis que vous longez le balcon en
fer forgé qui fait le tour de l'Arboretum, vous reconnaissez
soudain, dans la végétation, le feuillage d'un chêne du
Sommerlund et une vague de nostalgie vous serre le cœur. Mais,
loin de vous décourager, cette découverte décuple votre désir de
quitter au plus vite ce pays hostile et blanchi par le soleil. A l'une
des ouvertures donnant accès à l'Arboretum, vous découvrez un
Bâton appuyé contre le mur.
"""

fr_text_2 = """
Vous
quittez l'Arboretum et votre impatience croît tandis que vous
traversez un véritable dédale de couloirs froids et de vestibules
déserts. Vous parvenez ensuite à un palier, d'où une large cage
d'escalier descend vers une pièce occupant presque toute la
partie inférieure du Palais. Dissimulé en haut des marches dans
l'ombre d'un gros pilier, vous découvrez, avec une indicible
horreur, un spectacle qui vous glace le sang !
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_button("BÂTON", key="baton", label="Prendre le Bâton")
    st.write(fr_text_2)
    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_200.py", label="200", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
