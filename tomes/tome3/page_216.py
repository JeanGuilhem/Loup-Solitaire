import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=216, book=3)

fr_text = """
Vous avez parcouru 1,5 kilomètre environ lorsque vous apercevez
les premiers éclaireurs Barbares. Ils sont à skis et se trouvent au
nord. Tout d'abord vous ne voyez que deux de ces redoutables
guerriers, mais trois de leurs camarades les rejoignent bientôt.
Grands, la carrure particulièrement impressionnante, ils portent
des vêtements de fourrure. Quelques-uns d'entre eux sont
également équipés d'une armure en os. En dépit de leur taille, ils
glissent sur la neige avec une grâce et une rapidité presque
félines. Chacun d'eux s'est attaché dans le dos une longue
baguette à l'extrémité de laquelle flotte un petit drapeau.
Soudain, une flèche à la pointe d'os vous frôle le genou et vient se
ficher dans l'armature de bois du traîneau. Un instant plus tard,
un éclaireur Barbare passe à moins de 10 mètres de vous en
filant sur ses skis et vous avez le temps d'apercevoir son visage
aux pommettes saillantes et aux yeux bridés. Puis, tout à coup,
vous vous rendez compte que le Barbare porte un enfant sur le
dos. En fait, chacun des éclaireurs porte ainsi un enfant blotti
dans un sac à dos : c'est la raison pour laquelle leur carrure vous
semblait, de loin, si impressionnante. Ces enfants sont armés de
petits arcs en os et ils décochent des flèches en un tir nourri,
tandis que leurs pères se rapprochent de vous en glissant sur
leurs skis. Brusquement, Irian s'écroule, une flèche plantée dans
le dos. Dyce s'élance à son secours, mais il a à peine fait dix pas
qu'une autre flèche l'atteint à son tour. Fenor aussi est touché,
une flèche lui transperce la gorge. D'un pas chancelant, il essaie
courageusement de se maintenir debout pendant quelques
instants avant de s'effondrer dans la neige. Vous êtes seul, à
présent, tous vos guides sont morts. Un éclaireur Barbare passe
alors à votre gauche puis après un virage en épingle à cheveux, il
se met à foncer sur vous en pointant une longue lance à hauteur
de votre poitrine.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez combattre l'éclaireur Barbare, rendez-vous au :"))
    st.page_link("tomes/tome3/page_158.py", label="158", icon="📄")
    st.write_stream(stream_text("Si vous préférez tenter de vous enfuir, rendez-vous au :"))
    st.page_link("tomes/tome3/page_149.py", label="149", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
