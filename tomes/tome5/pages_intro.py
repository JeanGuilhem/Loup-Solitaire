import os

import streamlit as st
from environments import apply_environment
from inventory import display_inventory, init_state
from save import save_checkpoint, save_game
from utils import called_cookies, show_cover
from variable import BOOKS

BOOK = 5

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

init_state()
st.session_state.game_phase = "playing"
st.session_state.book = BOOK
st.session_state.current_page_number = 0
st.session_state.last_page_number = 0
apply_environment("ville")  # Holmgard, sous la neige, avant l'embarquement

st.title(f"📜 Tome {BOOK} — {BOOKS[BOOK]['title']}")
show_cover(BOOK)

fr_text = """
Vous êtes Loup Solitaire, le dernier des Seigneurs Kaï du
Sommerlund, et l'unique survivant du massacre qui les décima
au cours d'une guerre sans merci avec vos ennemis jurés : les
Seigneurs des Ténèbres d'Helgedad. C'est l'hiver, et un épais
manteau de neige recouvre les rues d'Holmgard, la capitale. Un
messager porteur d'un parchemin signé et scellé de la main du
roi Ulnar vient vous trouver dans votre monastère perdu au
milieu des collines. Vous êtes surpris par la lecture du message
du roi car il fait appel à votre aide pour résoudre un problème
qu'il décrit comme étant d'une « importance diplomatique
capitale ». Voilà une bien étrange requête adressée à un Seigneur
de la Guerre dont les talents sont plus utiles sur un champ de
bataille que dans les antichambres d'un palais pour parlementer
avec les envoyés de puissances étrangères. Cependant, vous
obéissez aux consignes et, à votre arrivée dans la capitale, tout
devient clair.
Le Zakhan de Vassagonie, le souverain de cet empire situé au
cœur du désert, a dépêché son plus fidèle envoyé afin de négocier
un traité de paix entre les deux pays, et vous avez été mandé pour
le signer au nom de votre roi. En effet, il y a un peu moins d'un
an, un noble de ce pays, nommé Barraka, a trahi son souverain et
a attaqué à la tête de son armée de brigands la province de
Ruanon, située au sud du Sommerlund. Cette ville minière et ses
environs ont été mis à sac et complètement détruits. Beaucoup
d'habitants du Sommerlund ont perdu la vie et les survivants ont
été réduits en esclavage et contraints de travailler dans les mines
des montagnes de Maaken. Quand il sut que le convoi régulier
n'était pas arrivé à la capitale, le roi vous envoya enquêter. Une
grande bataille s'ensuivit à l'issue de laquelle vous avez tué
Barraka. Sans votre courage et votre habileté, le Sommerlund et
toutes les régions des Fins de Terre auraient été exposés à de
graves dangers. Lorsque vous arrivez dans la grande salle du
trône, l'envoyé de Vassagonie est agenouillé aux pieds du roi et
lui dit d'une voix implorante :
— Votre Majesté, le Zakhan est désolé de l'infâme trahison de
Barraka et il attend avec anxiété que la confiance et l'amitié entre
nos deux pays soient rétablies. Il vous prie d'envoyer le Guerrier
Kaï, Loup Solitaire, au Grand Palais de Barrakeesh afin de signer
avec lui un traité de paix.
A la fin du discours, le roi se lève, dissimulant mal le dégoût que
lui inspire cet envoyé servile puis, se tournant vers vous, il vous
fait signe de le suivre dans l'intimité d'une antichambre.
— Je n'ai aucune sympathie pour ce royaume du désert, Loup
Solitaire, mais j'aime encore moins la perspective d'une guerre.
Le Zakhan est vieux, de constitution fragile et il n'a pas de fils
pour assurer sa succession. Barraka n'est qu'un des nombreux
nobles cruels et sans scrupules qui guettent comme des chacals la
moindre occasion pour s'emparer du pouvoir, et je crains qu'ils
n'attendent pas que leur empereur meure de mort naturelle. Ce
traité ne garantira peut-être pas la paix avec la Vassagonie, après
la mort du Zakhan, mais il permettra au moins de gagner un
temps précieux que nous mettrons à profit pour renforcer notre
frontière sud. Puis, le roi vous conduit à une fenêtre et il vous
montre le port, à peine visible à travers la neige qui tombe. Une
galère de Vassagonie mouille près des quais.
— Allez en
Vassagonie, Loup Solitaire, signez le traité et revenez
rapidement. Malgré cette promesse de paix, j'ai peur que l'ombre
menaçante de la guerre ne plane au-dessus de nos têtes avant
que l'année ne s'achève. Vous adressez un signe d'adieu à
Holmgard en cette morne journée d'hiver, persuadé que vous
serez de retour avant la fonte des neiges. Vous regardez les tours
de la ville disparaître peu à peu derrière un rideau de neige sans
vous douter des périls qui vous attendent en Vassagonie...
"""

tab1, tab2 = st.tabs(["Page", "Inventaire"])

with tab1:
    st.subheader("Traité de paix")
    st.write(fr_text)
    st.page_link("tomes/tome5/page_1.py", label="1", icon="📄")

with tab2:
    display_inventory()

if st.session_state.pop("checkpoint_pending", False):
    save_checkpoint()  # le héros pourra retenter ce tome depuis ici s'il meurt
save_game()
