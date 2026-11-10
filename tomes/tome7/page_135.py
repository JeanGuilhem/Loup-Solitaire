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

check_inventory(current_page_number=135, book=7)

fr_text = """
A la lumière d'un violent éclair vert, vous apercevez le toit
éventré de Kazan-Oud ; l'espace d'une fraction de seconde, vous
avez l'impression d'avoir sous les yeux la carcasse d'un
gigantesque lézard. Un second éclair vient illuminer les
nombreuses fenêtres du donjon qui semblent vous dévisager,
comme de grands yeux creux bordés d'éclats de vitres brisées.
Les remparts de pierre noire s'ornent d'une rangée de gargouilles
en surplomb de la jetée ; les têtes grimaçantes tiennent chacune
dans leur gueule un anneau de fer rouillé d'où partent de longues
cordes souillées de limon qui se balancent mollement au gré des
vagues. Le long de la jetée, l'eau est assez profonde pour
permettre à un gros vaisseau d'ancrer, mais les courants de fond
et la force de la marée rendent l'approche difficile pour un frêle
esquif tel que le vôtre. Vous réalisez soudain avec effroi que la
houle menace de vous écraser d'un moment à l'autre contre la jetée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez cesser de ramer pour essayer d'attraper l'une des cordes qui pendent, rendez-vous au :"))
    st.page_link("tomes/tome7/page_203.py", label="203", icon="📄")

    st.write_stream(stream_text("Si vous préférez abandonner votre bateau et vous jeter à l'eau pour gagner à la nage un banc de rochers un peu plus loin, à l'ouest, rendez-vous au :"))
    st.page_link("tomes/tome7/page_325.py", label="325", icon="📄")

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de l'Intuition, rendez-vous au :"))
    if has_magnakai("Intuition"):
        st.page_link("tomes/tome7/page_57.py", label="57", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome7/page_57.py", label="57", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
