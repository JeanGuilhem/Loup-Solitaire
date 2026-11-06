import streamlit as st
from inventory import (
    can_shoot,
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=224, book=6)

fr_text = """
« Par tous les diables ! s'écrie le Capitaine. Aurions-nous touché
le fond ?» Mais à peine a-t-il terminé sa phrase qu'un grappin
tombant du ciel vient s'accrocher au bastingage du bateau. Il est
suivi bientôt de beaucoup d'autres et vous pouvez distinguer
dans le brouillard les silhouettes de grandes chaloupes qui se
rapprochent rapidement. « Des pirates de rivière ! crie l'homme
à la barre. Préparez-vous à repousser l'assaut ! » Tout à coup, un
pirate lance un poignard qui atteint un des hommes du Capitaine
qui s'effondre à l'avant du pont. Ses camarades se précipitent à
son secours, mais les pirates sont déjà à bord et piétinent
sauvagement le corps du soldat. « En ordre de bataille ! » hurle le
Capitaine. Aussitôt ses hommes s'alignent en travers du pont,
lèvent leur bouclier et attendent l'ennemi de pied ferme. Un
groupe de pirates au visage féroce s'approche rapidement. L'un
d'entre eux, un homme maigre au nez cassé et qui n'a plus qu'une
oreille, vous adresse un large sourire en vous fixant de ses yeux
cruels. Il semble visiblement ravi à l'idée de vous ôter la vie.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez un Arc et que vous souhaitez l'utiliser, rendez-vous au :"))
    if can_shoot():
        st.page_link("tomes/tome6/page_170.py", label="170", icon="📄")
    else:
        st.write("*Il vous faut un Arc, un Carquois et une flèche.*")
        st.page_link("tomes/tome6/page_170.py", label="170", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous voulez vous préparer au combat par d'autres moyens, rendez-vous au :"))
    st.page_link("tomes/tome6/page_92.py", label="92", icon="📄")

    st.write_stream(stream_text("Enfin si vous préférez fuir le combat, rendez-vous au :"))
    st.page_link("tomes/tome6/page_286.py", label="286", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
