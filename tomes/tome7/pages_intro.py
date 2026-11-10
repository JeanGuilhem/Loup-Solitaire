import os

import streamlit as st
from environments import apply_environment
from inventory import display_inventory, init_state
from save import save_checkpoint, save_game
from utils import called_cookies
from variable import BOOKS

BOOK = 7

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

init_state()
st.session_state.game_phase = "playing"
st.session_state.book = BOOK
st.session_state.current_page_number = 0
st.session_state.last_page_number = 0
apply_environment("ville")  # Elzian, la cité des Anciens Mages

st.title(f"📜 Tome {BOOK} — {BOOKS[BOOK]['title']}")

fr_text = """
Vous êtes Loup Solitaire, le dernier des Seigneurs Kaï du
Sommerlund et l'unique survivant du massacre qui les décima au
cours d'une guerre sans merci avec vos ennemis jurés, les
Seigneurs des Ténèbres d'Helgedad. Il y a plusieurs siècles, Aigle
du Soleil, le premier Grand Maître Kaï, fonda l'Ordre du Kaï.
Avec l'aide des magiciens de Dessi, il parvint à réunir, à l'issue
d'une quête périlleuse, les sept cristaux de pouvoir appelés
Pierres de Nyxator. Grâce à ces sept pierres de la Sagesse, Aigle
du Soleil put avoir accès aux arcanes du savoir. Il consigna ses
découvertes et ses expériences dans un célèbre recueil connu
sous le nom du Livre du Magnakaï. Lors d'une précédente
aventure, vous avez retrouvé ce précieux volume dont on avait
depuis longtemps perdu la trace et vous avez fait le serment de
rendre au Kaï sa gloire et sa puissance de jadis, afin d'assurer une
paix durable au Sommerlund. Jusqu'à présent, l'étude du Livre
du Magnakaï ne vous a permis de maîtriser que quatre des dix
Disciplines Magnakaï. Pour atteindre votre but, il vous faudra
accomplir jusqu'au bout la tâche qu'Aigle du Soleil avait lui-
même entreprise il y a plus de mille ans. Si vous y parvenez, vous
acquérerez alors à votre tour le pouvoir et la sagesse recelés au
sein de chaque Pierre de Nyxator. Malheureusement, une grande
partie du manuscrit d'Aigle du Soleil s'est effacée avec le temps et
il ne reste plus que quelques bribes de phrases pour vous aider à
retrouver les sept pierres magiques. Guidé par les quelques mots
que vous êtes parvenu à décrypter çà et là, vous êtes parti un
beau matin pour la ville de Tekaro, une ville de Slovie qui se
trouvait alors en pleine guerre. C'est là que vous avez découvert
le premier cristal, la Pierre de la Sagesse de Varetta, cachée
depuis des siècles dans la crypte de la cathédrale. Alors que vous
serrez triomphalement le fabuleux cristal dans vos mains, vous
sentez son pouvoir se transmettre à vous et, simultanément,
l'emplacement de la deuxième pierre à trouver vous est aussitôt
révélé : Herdos. Herdos est un port établi sur les berges du lac
Khor, dans le lointain pays de Dessi, au fin fond des monts
Xulun. Ce sont les Anciens Mages de Dessi qui aidèrent jadis
Aigle du Soleil durant sa quête. Le temps a passé depuis, mais
voici venu le jour où ils vont être de nouveau sollicités par un
guerrier Kaï. « C'est le destin qui vous a conduit chez nous, Loup
Solitaire », déclare Rimoah, le représentant du Grand Conseil
des Anciens Mages, après que vous avez présenté votre requête
devant la docte assemblée réunie dans la Tour de la Vérité, à
Elzian. La voix claire et nette du magicien retentit à nouveau
dans la grande salle du Conseil : « Notre sort est
irrémédiablement lié au vôtre ! » A ces mots, les Anciens Mages
se rassemblent autour de vous et répondent solennellement
d'une seule et même voix : « Il en est ainsi ! »
Peu après, Rimoah vous conduit jusqu'à un espace circulaire qui
s'ouvre, tel un puits, dans le sol dallé de marbre vert. Après s'être
prudemment agenouillé au bord, il effleure la surface de métal
liquide de sa main gantée. Aussitôt, une onde frémissante
parcourt le fluide étincelant, et une étrange vision prend forme
au sein de ce miroir sans fond. Vous voyez se dessiner une
sinistre forteresse dressée sur une île rocheuse, dont l'ombre
menaçante se reflète dans les eaux noires d'un lac faiblement
éclairé par la lune. Vous avez devant vous Kazan-Oud. C'est dans
ce château que se trouve la Pierre de la Sagesse de Herdos,
emprisonnée derrière ces remparts maudits. « Nous vous
conduirons jusqu'à cette forteresse, Loup Solitaire, reprend
Rimoah, mais vous devrez ensuite y pénétrer seul, car nos
pouvoirs ne sont pas assez grands pour lutter contre les forces
maléfiques qui régissent ce redoutable endroit. En effet, peu
après la visite d'Aigle du Soleil en ces lieux, de puissantes forces
du mal s'abattirent sur Kazan-Oud. Nous n'avons pas pu les
anéantir, mais nous sommes toutefois parvenus à les contenir
dans un périmètre délimité, afin qu'elles ne gagnent pas notre
région. Mais combien de temps pourrons-nous encore tenir ?
Parmi les plus vaillants guerriers du Magnamund, nombreux
sont ceux qui ont tenté, à notre demande, de lutter contre le
pouvoir de Kazan-Oud, mais tous ont péri. Heureusement, le
destin nous amène aujourd'hui un Maître Kaï, et nos coeurs se
réjouissent à l'idée d'être bientôt débarrassés du fléau de Kazan-
Oud par une victoire éclatante sur les puissances maléfiques qui
le hantent. » Un murmure de satisfaction s'élève du cercle des
Anciens lorsque vous vous déclarez prêt à aller à Kazan-Oud
pour y accomplir votre mission. Quelques instants plus tard,
tandis qu'on prépare l'équipement dont vous aurez besoin lors de
votre dangereuse expédition, vous demandez la signification des
mots « Kazan-Oud ». Un silence pesant s'abat sur l'assemblée
des magiciens, et tous les regards se tournent vers Rimoah. « En
sommerlundois, répond-il d'une voix moins assurée, cela veut
dire Forteresse du mal...
"""

tab1, tab2 = st.tabs(["Page", "Inventaire"])

with tab1:
    st.subheader("Le Pays des Anciens Mages")
    st.write(fr_text)
    st.page_link("tomes/tome7/page_1.py", label="1", icon="📄")

with tab2:
    display_inventory()

if st.session_state.pop("checkpoint_pending", False):
    save_checkpoint()  # le héros pourra retenter ce tome depuis ici s'il meurt
save_game()
