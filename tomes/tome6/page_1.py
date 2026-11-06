import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    show_illustrations,
    show_map,
)
from text import fr_unknown_magnakai
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=1, book=6)

fr_text = """
Voici enfin venu le jour de votre départ. Tout est calme et
silencieux dans la cour du monastère Kaï, dont les remparts sont
couverts d'une mince couche de givre qui scintille dans la clarté
du petit matin. Un vent mordant souffle sur vous tandis que vous
engagez votre cheval sur le sentier escarpé qui descend vers la
forêt de Fryelund. Ce n'est qu'un peu plus tard que vous vous
retournez pour contempler les tours de pierre de votre imposante
demeure dont les hautes silhouettes s'élancent majestueusement
vers le ciel. Vous adressez en silence un dernier adieu au
monastère, puis vous pénétrez sous le couvert dense et feuillu de
la grande forêt. La longue traversée que vous effectuez vers le sud
ne se passe pas sans incident : sur la Route des Brigands - la
grande voie qui relie la capitale du Sommerlund à la province de
Ruanon -, vous vous faites soudainement attaquer par une horde
de hors-la-loi enragés. Mais au lieu de l'or qu'ils exigent, vous
leur faites une démonstration des formidables pouvoirs d'un
Maître Kaï digne de ce nom ! Décontenancés par la tournure
inattendue que prennent les événements et effarés par votre
remarquable talent de combattant, les bandits finissent par fuir
dans la plus grande confusion, abandonnant trois de leurs
comparses raides morts sur la route. A la suite de cet
affrontement, les personnages peu recommandables qui hantent
cette région morne et désolée se tiennent à une distance
respectueuse de vous, et vous poursuivez votre chemin sans être
inquiété de nouveau. Une fois arrivé à Ruanon, vous êtes
accueilli en véritable héros par la population et salué avec
reconnaissance par le Baron Vanalund, Seigneur de la province.
De fait, lui et son peuple n'oublieront jamais la dette qu'ils ont
envers vous, car vous avez jadis empêché leur pays de tomber
aux mains d'un cruel seigneur renégat. Les gens de Ruanon se
montrent si chaleureux à votre égard que votre quête risque de se
trouver fort compromise par la ronde interminable des banquets
et des réceptions organisés en votre honneur ! Mais il vous faut
malgré tout penser à votre devoir et il est grand temps
maintenant de quitter cette ville minière et ses aimables
habitants pour reprendre le chemin du sud. Il y a bien
longtemps, la route qui reliait Ruanon à Quarle fut coupée par un
effroyable tremblement de terre qui déchira le pays sur plusieurs
centaines de kilomètres. Cette gigantesque faille reçut le nom de
Gorges de Maaken -le Gouffre Maudit- car ses insondables
profondeurs sont l'objet d'une terrible malédiction. C'est là, en
effet, qu'au temps de la Lune Noire le roi Ulnar vainquit Vashna,
le plus puissant des Seigneurs des Ténèbres. Le corps du chef
ennemi ainsi que les cadavres de tous ses soldats furent
précipités dans les abîmes sans fond des Gorges de Maaken. La
légende raconte que l'écho du cri d'agonie de Vashna résonnera
jusqu'à ce qu'il se relève et puisse enfin exercer sa terrible
vengeance sur le royaume du Sommerlund et la maison d'Ulnar.
Tenant absolument à éviter le Gouffre Maudit, vous décidez de
faire un large détour par la ville libre de Casiorn plutôt que de
vous risquer à traverser la ville fantôme de Maaken. Peu à peu,
les plaines fertiles du sud de Ruanon font place à la végétation
pauvre et clairsemée des abords de la Mer de la Sécheresse. Là,
tel un joyau resplendissant au milieu du désert, se dresse la ville
libre de Casiorn. Vous y faites un séjour bref mais lucratif : grâce
à une chance inespérée - quelque peu aidée, il faut le reconnaître,
par vos qualités de Maître Kaï -, vous remportez des gains non
négligeables à la maison de jeu du Cercle d'Argent.
Grâce à la somme gagnée, vous allez effectuer quelques
emplettes et vous faites également l'acquisition d'un vigoureux
pur-sang pour chevaucher jusqu'à la ville de Quarle. Vous arrivez
une semaine plus tard dans les environs de Quarle et, à la tombée
du jour, vous en atteignez les remparts puissamment fortifiés. La
cité est construite au bord de la rivière du même nom, et c'est là
que se trouve le seul pont permettant de franchir les turbulentes
eaux. Non loin de l'enceinte, la route se sépare en deux car, du
côté est, on peut accéder à la ville par deux portes différentes.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez entrer par la porte nord, rendez-vous au :"))
    st.page_link("tomes/tome6/page_137.py", label="137", icon="📄")

    st.write_stream(stream_text("Si vous préférez aller vers la porte sud, rendez-vous au :"))
    st.page_link("tomes/tome6/page_225.py", label="225", icon="📄")

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de l'Exploration, rendez-vous au :"))
    if has_magnakai("Exploration"):
        st.page_link("tomes/tome6/page_308.py", label="308", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome6/page_308.py", label="308", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
