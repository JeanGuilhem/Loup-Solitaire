import os

import streamlit as st
from environments import apply_environment
from inventory import display_inventory, init_state
from save import save_checkpoint, save_game
from utils import called_cookies
from variable import BOOKS

BOOK = 3

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

init_state()
st.session_state.game_phase = "playing"
st.session_state.book = BOOK
st.session_state.current_page_number = 0
st.session_state.last_page_number = 0
apply_environment("ville")  # Holmgard, où le roi vous convoque

st.title(f"📜 Tome {BOOK} — {BOOKS[BOOK]['title']}")

fr_text = """
Au nord du royaume du Sommerlund, il est de tradition depuis
des siècles d'envoyer les fils des Seigneurs de la Guerre au
monastère Kaï. C'est là qu'on leur enseigne l'art et la science de
leurs nobles ancêtres.
Vous êtes le Loup Solitaire et le dernier Seigneur de la Guerre
que compte encore le Sommerlund. Il y a un an, les ennemis
irréductibles de votre peuple - les Maîtres des Ténèbres d'Helgedad -
ont envahi le royaume par surprise et
complètement détruit le monastère Kaï. Tous les Guerriers Kaï
qui y étaient rassemblés pour préparer la fête de Fehrman ont été
massacrés. Vous avez été le seul à échapper à la tuerie.
Vous avez alors regagné Holmgard, la capitale, en bravant bien
des périls et le roi vous a aussitôt confié une mission : vous
rendre dans le royaume ami de Durenor pour y demander une
aide urgente de vos alliés. Là encore, vous avez dû affronter
d'innombrables dangers, car le Sommerlund avait été trahi par
l'un de ses propres mages, Vonotar le Traître. Ses agents
cherchaient toutes les occasions de vous tuer, mais votre
intelligence et votre force ont eu raison de leur malfaisance.
Vous êtes donc revenu à la tête d'une puissante flotte - celle de vos
alliés de Durenor - et l'armée des Maîtres des Ténèbres qui
assiégeait la capitale a été mise en déroute.
Une grande partie du Sommerlund fut détruite par le conflit. De
riches terres arables n'étaient plus qu'étendues désolées et
plusieurs villes se trouvèrent entièrement rasées. Mais les
Sommerlundois sont un peuple courageux et l'énorme tâche de
reconstruction qu'ils avaient à accomplir ne les effrayait pas. Ils
entreprirent donc de rebâtir le Sommerlund dévasté avec une
telle détermination qu'à présent, un an plus tard, les traces de la
guerre ont presque complètement disparu.
Pour vous récompenser du rôle essentiel que vous avez joué dans
la victoire, le roi vous a accordé le rang et le titre de « Novicomte
du Sommerlund », une distinction rare pour quelqu'un d'aussi
jeune. Les ruines du monastère Kaï et la plupart des terres qui
l'environnent sont à présent un « Novicomté » placé sous votre protection.
Les travaux de reconstruction du monastère étaient sur le point
de commencer lorsque des nouvelles inquiétantes venues du
nord incitèrent le roi à vous convoquer dans la capitale. De
nombreux marchands, revenant de leurs expéditions d'été dans
les mers de Kalte, ont rapporté que le Brumalmarc - c'est le nom
que l'on donne au chef des Barbares des Glaces - avait été
renversé. Or, la description qu'ils ont faite du mage bossu qui a
succédé sur son trône au féroce tyran ne peut correspondre qu'à
un seul homme : Vonotar le Traître.
Après la défaite des Maîtres des Ténèbres, Vonotar alla se
réfugier dans les déserts glacés de Kalte. Il parvint jusqu'à la
Forteresse de Glace d'Ikaya où il réussit, par la ruse et la
tromperie, à convaincre le cruel Brumalmarc de le prendre à son
service comme mage officiel. De la part du chef barbare, ce fut là
une grave erreur qui lui coûta tout à la fois sa forteresse et la vie.
La nouvelle que Vonotar serait toujours actif se répand comme
une traînée de poudre dans tout le royaume du Sommerlund.
Des milliers de citoyens se sont rassemblés autour de la capitale
pour exiger qu'on fasse payer à Vonotar le prix de sa trahison.
L'agitation est telle que le roi se voit contraint de promettre que
l'infâme traître sera ramené à Holmgard pour y répondre de ses
crimes. Et pour vous, Loup Solitaire, la promesse du roi marque
le commencement d'une quête qui va vous confronter à un
ennemi détesté entre tous en vous plongeant dans de redoutables
profondeurs : celles des Grottes de Kalte.
"""

tab1, tab2 = st.tabs(["Page", "Inventaire"])

with tab1:
    st.subheader("Vonotar le Traître")
    st.write(fr_text)
    if os.path.exists("tomes/tome3/page_1.py"):
        st.page_link("tomes/tome3/page_1.py", label="1", icon="📄")
    else:
        st.info(
            "La suite du tome 3 est en cours d'adaptation. Votre héros est sauvegardé : "
            "revenez bientôt pour partir à Kalte !"
        )
        st.page_link("accueil.py", label="Retour à l'accueil", icon="🏠")

with tab2:
    display_inventory()

if st.session_state.pop("checkpoint_pending", False):
    save_checkpoint()  # le héros pourra retenter ce tome depuis ici s'il meurt
save_game()
