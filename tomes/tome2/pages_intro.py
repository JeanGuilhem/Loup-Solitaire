import os

import streamlit as st
from environments import apply_environment
from inventory import display_inventory, init_state
from save import save_game
from utils import called_cookies
from variable import BOOKS

BOOK = 2

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

init_state()
st.session_state.game_phase = "playing"
st.session_state.book = BOOK
st.session_state.current_page_number = 0
st.session_state.last_page_number = 0
apply_environment("ville")  # Holmgard, avant l'embarquement

st.title(f"📜 Tome {BOOK} — {BOOKS[BOOK]['title']}")

fr_text = """
Au nord du royaume du Sommerlund, il est de tradition depuis des
siècles d'envoyer les fils des Seigneurs de la Guerre au monastère Kaï.
C'est là qu'on leur enseigne l'art et la science de leurs nobles ancêtres.
Au temps jadis, à l'époque de la Lune Noire, les Maîtres des Ténèbres
menèrent une guerre sans merci contre le royaume du Sommerlund. Ce
fut une longue et douloureuse épreuve de force à l'issue de laquelle les
guerriers du Sommerlund remportèrent la victoire lors de la grande
bataille de Maaken. Le roi Ulnar et ses alliés de Durenor anéantirent
l'armée des Maîtres des Ténèbres dans le défilé de Moytura et
précipitèrent l'ennemi au fond du gouffre de Maaken. Vashna, le plus
puissant parmi les Maîtres des Ténèbres, périt d'un coup mortel que le
roi Ulnar lui porta de sa puissante épée, l'épée du soleil, que l'on
désigne généralement sous le nom de «Glaive de Sommer». Depuis ce
temps, les Maîtres des Ténèbres ont juré de prendre leur revanche sur le
royaume du Sommerlund et la Maison d'Ulnar.
Quant à vous, vous êtes le Loup Solitaire, un disciple du Temple Kaï où
l'on vous a initié aux secrets des
Seigneurs de la Guerre. Or, il y a deux jours, le paisible royaume s'est
trouvé plongé dans la tourmente à la suite de l'invasion soudaine du
pays par une puissante armée que commandaient les Maîtres des
Ténèbres. Au cours de l'attaque, le monastère Kaï a été complètement
détruit et les Seigneurs qui s'y étaient réunis pour préparer la grande
fête de Fehmarn ont tous été tués lors des combats ; les murs du temple
se sont écroulés sur eux, les écrasant sous les décombres. Vous êtes le
seul Seigneur Kaï à avoir échappé au massacre et vous avez juré de
venger la mort de vos compagnons. Votre première tâche était d'avertir
le roi car, en l'absence des Seigneurs Kaï à la tête de l'armée, il devenait
impossible de mobiliser à temps la population pour repousser les
Maîtres des Ténèbres.
Vous avez affronté de grands périls en vous rendant auprès du
souverain ; l'ennemi avait déjà soumis la plus grande partie du royaume
et son armée s'avançait vers Holmgard, la capitale, mais, en dépit du
danger et au prix de rudes combats, vous avez réussi à atteindre le
Palais et à prévenir le roi. A la cour, on a fait l'éloge de votre habileté et
de votre bravoure mais on vous a également averti que votre mission
était loin d'être terminée : à présent que les Seigneurs Kaï sont morts, il
n'y a plus, sur toutes les terres de Magnamund, qu'une seule force assez
puissante pour venir à bout des Maîtres des Ténèbres et cette force,
c'est celle du Glaive de Sommer.
Or, après la défaite de Vashna, le Glaive de Sommer fut offert aux
alliés de Durenor comme un symbole de la confiance et de la solidarité
qui unit les deux royaumes. En échange, le roi Alin de Durenor fit
présent au Sommerlund d'un magnifique anneau d'or frappé du sceau
royal de son pays. Cet anneau porte le nom de « Sceau d'Hammardal ».
Lors de la cérémonie, le roi Alin jura que le royaume de Durenor
viendrait aussitôt en aide à son allié si jamais le Sommerlund se
trouvait à nouveau menacé par l'ombre des Ténèbres venue de
l'occident.
Le roi vous a confié le Sceau d'Hammardal et votre mission consiste
désormais à vous rendre au royaume de Durenor pour y chercher le
Glaive de Sommer. Mais entre temps, les troupes ennemies ont réussi à
forcer les lignes de défense de la capitale et s'apprêtent à assiéger la
ville. Tandis que le capitaine Gayal, de la Garde du Roi, vous conduit à
l'arsenal du Palais pour y prendre les armes que vous emporterez dans
votre quête, les dernières paroles de votre souverain vous reviennent
sans cesse à l'esprit : « Quarante jours, Loup Solitaire, tu n'as que
quarante jours pour rapporter le glaive. Nous aurons la force de résister
à l'ennemi pendant ces quarante jours. Après... Il sera trop tard... »
Le capitaine Gayal et ses gardes vous escortent jusqu'aux portes de la
citadelle : là, un chariot bâché vous attend. Dès que vous y avez pris
place, les portes s'ouvrent et le chariot se fraie un chemin dans les rues
populeuses de Holmgard, la capitale du Sommerlund. Le voyage est
court, mais très inconfortable. Bientôt, le chariot s'arrête et le
conducteur vient écarter les pans de la bâche qui vous dissimule aux
regards. « Voici le quai d'embarquement, Seigneur Kaï, annonce le
conducteur du chariot, et voici votre navire, le Sceptre Vert. »
"""

tab1, tab2 = st.tabs(["Page", "Inventaire"])

with tab1:
    st.subheader("Quarante jours pour un Loup Solitaire")
    st.write(fr_text)
    if os.path.exists("tomes/tome2/page_1.py"):
        st.page_link("tomes/tome2/page_1.py", label="1", icon="📄")
    else:
        st.info(
            "La suite du tome 2 est en cours d'adaptation. Votre héros est sauvegardé : "
            "revenez bientôt pour partir à Durenor !"
        )
        st.page_link("accueil.py", label="Retour à l'accueil", icon="🏠")

with tab2:
    display_inventory()

save_game()
