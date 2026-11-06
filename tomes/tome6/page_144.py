import streamlit as st
from inventory import (
    check_inventory,
    choose_item_to_lose,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=144, book=6)

fr_text = """
Le dortoir est une pièce mansardée, longue et étroite, située à
l'arrière de l'auberge. Il y règne une forte odeur de sueur, et
les ronflements des mercenaires forment un véritable concert.
Vous choisissez une paillasse près de la fenêtre : mieux vaut
encore affronter le vent qui souffle à travers l'encadrement mal
ajusté que respirer la puanteur ambiante ! Au beau milieu de la
nuit, vous êtes réveillé par une vive lumière. Par la fenêtre,
vous apercevez alors une magnifique étoile filante dont la
splendeur illumine toute la ville pendant un bref instant,
projetant au passage un faisceau de lumière irisé sur le morne
dortoir. Vous admirez la comète jusqu'à ce qu'elle s'évanouisse
au loin dans les ténèbres de la nuit, puis vous vous recouchez.
Lorsque le tintement agressif de la cloche du dortoir se met à
retentir, vous éprouvez la désagréable sensation d'avoir à peine
dormi quelques minutes. « Debout tout le monde, debout ! Voici
venir un jour nouveau, mes braves ! » La voix tonitruante de
l'aubergiste est rapidement couverte par les grognements
mécontents d'une bonne centaine de soldats à l'air hagard qui se
mettent péniblement sur leur séant. Vous vous habillez
rapidement, vous rassemblez vos affaires, puis vous allez
chercher votre cheval à l'écurie. Vous étudiez ensuite le trajet
pour vous rendre à la rue des Chaudronniers, mais vous constatez
avec consternation qu'il manque un Objet dans votre Sac à Dos :
quelqu'un a dû vous le voler pendant la nuit. Supprimez l'un de
vos Objets - au choix - sur votre Feuille d'Aventure, puis
mettez-vous en route pour la rue des Chaudronniers.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if choose_item_to_lose(list(st.session_state.backpack), key="vol", label="Choisissez l'Objet qu'on vous a volé :"):
        st.write_stream(stream_text("Rendez-vous au :"))
        st.page_link("tomes/tome6/page_300.py", label="300", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
