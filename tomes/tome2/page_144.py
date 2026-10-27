import streamlit as st
from inventory import (
    add_to_inventory,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    lose_gold,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=144, book=2)

fr_text = """
Un grand Noudic vêtu d'une cape de soie en patchwork aux couleurs
vives ordonne à quelques-uns de ses congénères de prendre leurs armes
et de vous reconduire au-dehors. Vous leur parlez alors dans leur
propre langue et un murmure de stupeur parcourt aussitôt la caverne.
Jamais encore ils n'ont rencontré d'être humain qui sache parler leur
dialecte. Certains d'entre eux en sont abasourdis au point de vous
contempler bouche bée, les yeux ronds et les pattes ballantes. Le grand
Noudic s'adresse alors à vous en se présentant comme le chef de la
colonie. Il déclare se nommer Gashiss et vous souhaite la bienvenue en
vous invitant à le rejoindre sur une estrade dressée au centre de la
caverne. « Vouzz n'êtezz pazz de Dzurzenorz, vouzz l'homme-là,
heinzz ? vous demande-t-il avec un fort accent noudic, d'ouzz venezz
vouzz donczz ? » Vous lui dites que vous êtes sommerlundois et que
vous vous rendez à Hammardal. Le Noudic alors vous jette un regard
inquiet. « Vouzz n'êtezz pazz unzz Zombizarre, au moinzz, j'espèrezz?»
demande-t-il d'une voix anxieuse. Vous comprenez aussitôt que le mot
« Zombizarre » désigne les Monstres d'Enfer dans la langue noudic et il
vous apprend bientôt que deux de ces créatures malfaisantes sont
arrivées à Tarnalin il y a deux heures et ont provoqué une panique
générale dans le tunnel. Gashiss sait où ces deux monstres se cachent;
ils vous attendent pour vous tendre une embuscade. « Vouzz voulezz
que je vouzz montrezz commentzz lezz évitezz, vouzz, l'homme-là,
heinzz ? » propose-t-il. Vous acceptez volontiers cette offre et il vous
fait signe de le suivre au bas de l'estrade. Les Noudics à présent ont
surmonté leur stupeur et ils semblent vous considérer comme l'un
d'eux. Avant que vous ne quittiez la caverne, une jolie femelle noudic
vous offre quelques provisions. Il y a là l'équivalent de 2 Repas. Vous
la remerciez de sa générosité et vous suivez Gashiss le long d'un des
nombreux couloirs qui partent de la caverne. Au bout d'une heure de
marche dans l'obscurité, il s'arrête et vous montre un rayon de lumière
qui filtre par une crevasse à quelque distance. « Enzz sortantzz par làzz,
vouzz n'aurezz plus rienzz à craindre, vouzz, l'homme-là, heinzz ! »
déclare votre guide. Vous le remerciez de vous avoir aidé mais vous
remerciez surtout en votre for intérieur les Maîtres Kaï qui vous ont
enseigné la Discipline de la Communication Animale. Ces longues
années d'apprentissage vous ont sans doute sauvé la vie. Vous vous
faufilez bientôt par une crevasse de la paroi rocheuse et vous vous
laissez tomber sur la chaussée qui longe le mur à un mètre au-dessous.
Les Noudics se sont montrés fort serviables et vous leur en êtes très
reconnaissant jusqu'au moment où vous vous apercevez qu'il ne vous
reste plus une seule Pièce d'Or ! Ils vous ont tout dérobé et vous n'avez
plus qu'à modifier votre Feuille d'Aventure en conséquence.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        add_to_inventory("REPAS", quantity=2)  # les provisions de la femelle noudic
        lose_gold()  # les Noudics vous ont tout dérobé
    st.metric(label="Couronnes", value=st.session_state.purse)
    st.write_stream(stream_text("Vous vous trouvez toujours dans le tunnel de Tarnalin que vous continuez à suivre en vous rendant au :"))
    st.page_link("tomes/tome2/page_349.py", label="349", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
