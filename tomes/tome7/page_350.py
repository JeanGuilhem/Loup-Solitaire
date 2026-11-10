import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=350, book=7)

fr_text = """
Vous avez à peine franchi le bouclier protecteur que vous êtes
accueilli en héros par la flotte tout entière des navires marchands
et des bateaux de pêche du Dessi. Une heure auparavant, en
assistant à l'éruption de Kazan-Oud, les habitants de Herdos ont
compris que le fléau qui hantait et menaçait leur pays depuis des
siècles était enfin détruit. Les embarcations de la ville se sont
donc dirigées aussitôt, toutes voiles dehors, vers le bouclier. La
foule ovationne maintenant le guerrier du Sommerlund qui a
réussi à les délivrer de l'ombre malfaisante, et vous êtes hissé à
bord de la caravelle du seigneur Ardan où vous êtes salué par les
trompettes de ses gardes Vakeros. « Nous vous serons toujours
reconnaissants, Loup Solitaire, dit Ardan d'une voix brisée par
l'émotion en vous serrant la main en signe d'amitié et de
gratitude. » Puis il poursuit sous les acclamations de son peuple :
« Vous avez accompli ce que nous croyions être impossible. Votre
bravoure est un exemple pour nous tous et cet exploit entrera
dans la légende ! » Il vous interroge ensuite sur votre propre
mission. Vous sortez alors la Pierre de la Sagesse de Herdos de la
poche de votre tunique déchirée. Il regarde la pierre, les yeux
agrandis par la surprise, puis il incline la tête et vous dit d'une
voix solennelle et respectueuse : « Mon Seigneur, vous êtes au
summum de la gloire ! Votre but et votre destinée sont connus
des Anciens Mages, car nous attendions votre venue depuis des
milliers d'années. Notre survie et celle de tout ce que nous
chérissons dépendent du succès de votre quête du Magnakaï. Le
temps est venu, Loup Solitaire, que nous vous transmettions
notre sagesse, puisque nous sommes, vous et moi, du même sang
et que nos destins sont liés. La Pierre de la Sagesse que vous
devez chercher maintenant se trouve dans un pays qui fut
autrefois notre patrie ; au cœur de notre ancien temple, qui était
autrefois notre lieu le plus sacré, là même où notre maître nous
apparut pour la première fois. » Vous avez rempli votre mission
avec succès et les pouvoirs de la Pierre de Herdos se sont
transmis à votre corps et à votre esprit. Sa force et sa sagesse font
désormais partie intégrante de vous-même, mais il vous reste
encore beaucoup à apprendre des Anciens Mages. Ils vous
prépareront à la quête Magnakaï la plus difficile que vous ayez
jamais entreprise et qui vous mènera au cœur des marais hostiles
de Danarg, où vivent encore les créatures d'Agarash le Damné,
qui régnent en maître sur le pays. Si vous avez le courage d'un
maître Kaï digne de ce nom, les secrets des Anciens Mages et les
périls du Danarg vous attendent dans le prochain volume de la
série Loup Solitaire !
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        st.balloons()
    st.success(
        "**Mission accomplie !** Kazan-Oud s'est effondrée, la Pierre de la Sagesse de Herdos est à vous et ses "
        "pouvoirs se sont transmis à votre corps et à votre esprit : votre quête du Magnakaï peut se poursuivre."
    )
    st.info("Le tome 8 (« La Jungle des Horreurs ») n'est pas encore disponible dans l'application.")
    st.page_link("accueil.py", label="Retour à l'accueil", icon="🏠")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
