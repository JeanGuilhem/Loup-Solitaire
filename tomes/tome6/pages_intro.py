import os

import streamlit as st
from environments import apply_environment
from inventory import display_inventory, init_state
from save import save_checkpoint, save_game
from utils import called_cookies, show_cover
from variable import BOOKS

BOOK = 6

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

init_state()
st.session_state.game_phase = "playing"
st.session_state.book = BOOK
st.session_state.current_page_number = 0
st.session_state.last_page_number = 0
apply_environment("montagne")  # le monastère Kaï, au départ vers le sud

st.title(f"📜 Tome {BOOK} — {BOOKS[BOOK]['title']}")
show_cover(BOOK)

fr_text = """
Vous êtes Loup Solitaire, le dernier des Seigneurs Kaï du
Sommerlund et l'unique survivant du massacre qui les anéantit
au cours d'une guerre sans merci avec vos ennemis jurés, les
Seigneurs des Ténèbres d'Helgedad. Trois années se sont
écoulées depuis votre victoire écrasante sur le Seigneur des
Ténèbres Haakon, dans le Tombeau du Majhan. Pour le royaume
du Sommerlund, ce furent trois années de paix et de prospérité.
Par ailleurs, depuis la défaite de Haakon, le pouvoir des
Seigneurs des Ténèbres s'est peu à peu dégradé. La rumeur court
qu'une guerre civile dévastatrice fait rage à Helgedad, où même
les Seigneurs des Ténèbres les plus insignifiants se livrent à une
rivalité sans merci pour conquérir le pouvoir et assouvir leurs
sinistres ambitions. Cependant, nul n'ignore que la véritable
raison de cette course au pouvoir tient à la découverte d'un trésor
perdu depuis la nuit des temps : le Livre du Magnakaï du
Sommerlund. Ce livre légendaire est célèbre dans votre pays. En
effet, grâce à la sagesse du Magnakaï, Aigle du Soleil, le premier
Grand Maître Kaï, parvint à enseigner aux guerriers du
Sommerlund les Disciplines qui devaient protéger le pays de la
ruine et l'empêcher de tomber aux mains des maléfiques
Seigneurs des Ténèbres.
On perdit la trace du Livre du Magnakaï pendant des centaines
d'années, mais la science qu'il recelait demeura vivante dans les
esprits, se transmettant de génération en génération afin que les
guerriers Kaï puissent acquérir la force et le pouvoir de résister
aux ennemis de leur pays.
Après avoir retrouvé le Livre au Magnakaï, vous fîtes une
promesse solennelle : rendre au Kaï sa gloire et sa puissance de
jadis afin de garantir une paix et une sécurité durables au
Sommerlund. De retour dans votre pays, vous vous êtes
entièrement consacré à l'étude des Disciplines Magnakaï, vivant
comme un reclus dans votre monastère perdu au milieu des
collines. L'apprentissage fut long et astreignant car il consistait
aussi bien en un entraînement physique intense qu'en une
éducation psychique et intellectuelle poussée au plus haut
niveau. Les saisons se succédèrent sans que vous voyiez le temps
passer tant vous étiez absorbé par votre désir d'accéder aux
arcanes de la connaissance et au perfectionnement de vos
qualités guerrières. Vous êtes ainsi resté trois ans à maîtriser
parfaitement trois des disciplines Magnakaï. Cependant les
autres disciplines ne peuvent s'acquérir par l'étude uniquement
et, afin d'accomplir votre serment de porter à nouveau la
philosophie Kaï à son apogée, il vous faut maintenant poursuivre
l'œuvre entamée par Aigle du Soleil, il y a de cela quelque mille
ans. Lorsque ce dernier eut achevé sa quête, il consigna ses
expériences dans le Livre du Magnakaï. Malheureusement, le
texte s'est effacé avec les années, et il n'en reste plus que
quelques mots : «... chercher à retrouver la Pierre de la Sagesse
de Varetta..., car seule cette pierre détient le pouvoir et la
sagesse... » Voici les seules bribes de phrases que vous êtes
parvenu à déchiffrer, ce qui est bien peu pour vous guider !
Cependant, malgré tout, vous ne perdez pas espoir, car vous avez
reconnu le mot « Varetta ». Il s'agit d'une des plus anciennes
cités du Magnamund. Elle se trouve de l'autre côté des Gorges de
Maaken, au sud du Sommerlund, en plein pays de la Storn. Vous
sentez qu'il vous faut partir sans plus attendre, car la guerre
civile dans laquelle sont empêtrés les Seigneurs des Ténèbres de
Helgedad ne se prolongera pas éternellement. Vous savez
également que ceux-ci n'ont qu'une idée en tête : conquérir le
Sommerlund et le tenir sous leur coupe. Dès le conflit calmé, les
misérables vainqueurs se retourneront aussitôt contre votre pays
et convoqueront les créatures du Royaume des Maudits pour
compromettre votre quête. Il vous faut donc agir rapidement et
discrètement car l'avenir du Sommerlund dépend du succès de
votre mission. Ainsi, avec pour seul guide les derniers mots de
votre mentor et sous la menace constante des Seigneurs des
Ténèbres, vous décidez de partir à la recherche de la Pierre de la
Sagesse de Varetta, sans vous douter des périls et des imprévus
qui vous attendent dans les pays de la Storn.
"""

tab1, tab2 = st.tabs(["Page", "Inventaire"])

with tab1:
    st.subheader("L'avenir du Sommerlund est entre vos mains")
    st.write(fr_text)
    st.page_link("tomes/tome6/page_1.py", label="1", icon="📄")

with tab2:
    display_inventory()

if st.session_state.pop("checkpoint_pending", False):
    save_checkpoint()  # le héros pourra retenter ce tome depuis ici s'il meurt
save_game()
