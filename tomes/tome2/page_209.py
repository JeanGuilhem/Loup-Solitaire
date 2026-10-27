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

check_inventory(current_page_number=209, book=2)

fr_text = """
Vous entendez bientôt des murmures parmi les hommes d'équipage.
Parfois, quelques mots prononcés distinctement vous parviennent aux
oreilles : ils parlent de « vaisseaux fantômes » et de « malédiction »,
mais les rumeurs s'évanouissent brusquement lorsque la voix tonnante
du capitaine appelle tout le monde sur le pont. Et lorsque le capitaine
Kelman monte lui-même sur le pont arrière pour venir parler à
l'équipage, on n'entend plus alors que le craquement des mâts du navire
qui gémissent sous le vent. « Nous sommes à trois jours de Port Bax,
dit le capitaine. Le feu a dévoré nos provisions et nous n'avons plus
d'eau potable. Il nous faut donc mettre le cap sur Ragadorn où nous
pourrons faire réparer le navire et reconstituer nos vivres. C'est tout. »
Les hommes d'équipage semblent satisfaits de cette décision et ils se
remettent au travail avec une vigueur renouvelée. Le capitaine se tourne
alors vers vous. « Nous aurons rallié le port de Ragadorn dans huit
heures environ, dit-il. J'ai reçu pour instructions de vous amener sain et
sauf à Port Bax et de vous confier à la garde du Consul du
Sommerlund, le Lieutenant Général Rhygar. Mais le temps est contre
nous et j'ai bien peur qu'il faille une bonne huitaine de jours pour
réparer le navire. Lorsque nous aurons jeté l'ancre, vous devrez alors
décider si vous souhaitez poursuivre votre voyage à Durenor par la mer
en restant avec nous ou par la route en allant là-bas par vos propres
moyens. » Tandis que vous retournez dans votre cabine, les paroles du
roi vous reviennent en mémoire : « Quarante jours, Loup Solitaire, tu
n'as que quarante jours pour rapporter le Glaive. Nous aurons la force
de résister à l'ennemi pendant ces quarante jours. Après... il sera trop
tard... » Non, décidément, il ne vous reste guère de temps pour
accomplir votre périlleuse mission.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome2/page_197.py", label="197", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
