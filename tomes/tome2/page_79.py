import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=79, book=2)

fr_text = """
Une puissante énergie se répand dans votre corps avec une telle force
que vous en oubliez tout ce qui vous entoure. Instinctivement, vous
levez le Glaive au-dessus de votre tête ; un rayon de soleil vient alors
frapper l'extrémité de sa lame et une lumière blanche, aveuglante, jaillit
aussitôt dans toute la pièce. C'est à ce moment précis que le véritable
pouvoir du Glaive de Sommer se révèle à vous dans toute son ampleur.
Cette arme a été forgée bien avant que les Sommerlundois, les
Durenorais et les Maîtres des Ténèbres se soient installés sur les
territoires des Fins de Terre. Ceux qui ont fabriqué le Glaive
appartiennent à une lignée que les hommes appelleraient des dieux et
seul un Seigneur Kaï peut déployer la puissance de cette arme
exceptionnelle : si quiconque d'autre s'en servait pour combattre, cette
puissance faiblirait et finirait par disparaître à jamais. Lorsque vous en
ferez usage lors d'un combat, le Glaive de Sommer ajoutera 8 points à
votre total d'HABILETÉ et 10 points si vous avez choisi la Discipline
Kaï de la Maîtrise des Armes (bien entendu, il faudra, dans ce cas, que
la Table de Hasard vous ait donné cette maîtrise à l'épée). Le Glaive a
le pouvoir de rendre nulle toute pratique magique exercée par un
ennemi contre celui qui le brandit ; en outre, si vous devez affronter des
créatures de l'au-delà, des Monstres d'Enfer par exemple, tous les points
d'ENDURANCE perdus par vos adversaires au cours des combats
seront multipliés par 2 : telle est la puissance du Glaive de Sommer.
Enfin, c'est la seule arme, au nord de Magnamund, qui puisse tuer un
Maître des Ténèbres et c'est pourquoi vos ennemis feront tout pour
empêcher le succès de votre mission. Vous avez pleinement
conscience, à présent, de tenir entre vos mains le salut de votre peuple
car nul autre pouvoir que celui du Glaive ne parviendra à lui donner la
victoire. Peu à peu, la lumière blanche et aveuglante s'évanouit et vous
sentez alors peser sur votre épaule la main de Lord Axim. « Venez,
Loup Solitaire, dit-il, car il y a maintenant beaucoup à faire pour
préparer votre retour au Royaume du Sommerlund. » Vous rangez le
Glaive dans son fourreau incrusté de pierreries et vous suivez Lord
Axim qui sort de la chambre du roi. Apportez les modifications
nécessaires à votre total d'HABILETÉ, en fonction des indications qui
viennent de vous être données, et notez les pouvoirs que vous confère
le glaive dans la case Objets Spéciaux de votre Feuille d'Aventure.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.info("Les bonus du Glaive de Sommer sont appliqués automatiquement lors des combats.")

    st.write_stream(stream_text("Rendez-vous ensuite au :"))
    st.page_link("tomes/tome2/page_40.py", label="40", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
