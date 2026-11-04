import streamlit as st
from inventory import (
    buy_button,
    check_inventory,
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

check_inventory(current_page_number=154, book=5)

fr_text = """
Vous écartez le rideau de perles et vous pénétrez dans une pièce
fraîche plongée dans une semi-obscurité. Les fenêtres sont
masquées par toutes sortes d'herbes et de plantes qui tamisent la
lumière. Vous examinez une curieuse rangée de bocaux colorés
lorsqu'une femme apparaît. Elle a des yeux verts perçants et ses
cheveux roux sont relevés en arrière, maintenus par des anneaux
de jade. Elle vous adresse la parole d'une voix douce :
« Bienvenue, Homme du Nord, je suppose que vous êtes un
guerrier, ou est-ce que je me trompe ? » Alors que vous hésitez à
répondre, elle hausse les épaules puis elle fouille dans une pile de
parchemins posés sur un tonneau de vin. Elle souffle la poussière
d'une feuille jaunie, puis vous la tend : c'est une liste de
marchandises, rédigée en sommerlundais. Vous lisez :

- Potion d'Alether (qui augmente le total d'HABILETÉ de 4 points
pour la durée d'un combat) : 4 Pièces d'Or.
- Potion de l'herbe à Potence (chaque dose procure un sommeil
d'une ou deux heures) : 2 Pièces d'Or.
- Potion de Laumspur (chaque dose fait gagner 4 points
d'ENDURANCE) : 5 Pièces d'Or.
- Fiole d'huile de Larnuma (chaque dose donne 2 points
d'ENDURANCE) : 3 Pièces d'Or.
- Teinture de chiendent des Cimetières (1 dose rend malade et fait
perdre 2 points d'ENDURANCE) : 1 Pièce d'Or.
- Teinture de Calacena (1 dose produit de terribles hallucinations
pendant une heure ou deux) : 2 Pièces d'Or.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Vous pouvez acheter ce que vous désirez dans la liste ci-dessus ; inscrivez les potions, fioles, teintures que vous prenez sur votre Feuille d'Aventure dans la case Sac à Dos."))
    for dose in (1, 2, 3):
        buy_button("POTION D'ALETHER", 4, key=f"alether_{dose}", label="Acheter une Potion d'Alether (4 Couronnes)")
    for dose in (1, 2, 3):
        buy_button("POTION D'HERBE À POTENCE", 2, key=f"potence_{dose}", label="Acheter une Potion d'herbe à Potence (2 Couronnes)")
    for dose in (1, 2, 3):
        buy_button("POTION DE LAUMSPUR", 5, key=f"laumspur_{dose}", label="Acheter une Potion de Laumspur (5 Couronnes)")
    for dose in (1, 2, 3):
        buy_button("HUILE DE LARNUMA", 3, key=f"larnuma_{dose}", label="Acheter une Fiole d'huile de Larnuma (3 Couronnes)")
    for dose in (1, 2, 3):
        buy_button("POTION DE RONCES DES CIMETIÈRES", 1, key=f"cimetieres_{dose}", label="Acheter une Teinture de chiendent des Cimetières (1 Couronne)")
    for dose in (1, 2, 3):
        buy_button("TEINTURE DE CALACENA", 2, key=f"calacena_{dose}", label="Acheter une Teinture de Calacena (2 Couronnes)")
    st.write_stream(stream_text('Vous pouvez ensuite quitter la boutique et continuer à avancer dans la rue. Rendez-vous au :'))
    st.page_link("tomes/tome5/page_179.py", label="179", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
