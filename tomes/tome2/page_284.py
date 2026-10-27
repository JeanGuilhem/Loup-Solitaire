import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies, handle_repas

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=284, book=2)

fr_text = """
Les soldats vous encerclent et confisquent votre Sac à Dos et vos armes
; puis le chevalier s'avance vers vous et lève la visière de son heaume. «
Qui êtes-vous ? Que venez vous faire à Tarnalin ? » demande-t-il d'une
voix rude. Vous lui répondez que vous êtes un Seigneur Kaï du
Sommerlund porteur d'un message urgent destiné au roi Alin. Il ne
semble pas très convaincu jusqu'au moment où vous lui montrez le
Sceau d'Hammardal. Dès lors, sans la moindre hésitation, il ordonne à
ses hommes de vous rendre votre bien et il vous fait franchir le barrage
de chariots. Derrière, un carrosse est stationné, au milieu du tunnel
encombré. «A Hammardal, et vite ! » ordonne-t-il au cocher en vous
entraînant à l'intérieur. Vous avez à peine eu le temps de vous asseoir
que les chevaux s'élancent au grand galop. Le chevalier vous apprend
bientôt qu'il se nomme Lord Axim de Ryner et qu'il est le commandant
de la garde personnelle du roi. Il se rendait à Port Bax lorsque les
Monstres d'Enfer ont envahi le tunnel. La terrible bataille qui s'est
ensuivie n'a laissé dans ses rangs que onze rescapés : lui-même et dix
de ses soldats. La faim vous tenaille tandis que vous filez dans le tunnel
de Tarnalin et il vous faut prendre aussitôt un Repas, sinon, vous
perdrez 3 points d'ENDURANCE. Le voyage jusqu'à la capitale durera
cinq heures et Lord Axim vous conseille de vous reposer quelque peu
d'ici à votre arrivée. Vous vous laissez alors gagner par le sommeil et
dans un songe vous vous voyez revenir triomphalement à Holmgard en
brandissant le Glaive de Sommer ; la suite du rêve vous montre la
défaite cuisante des Maîtres des Ténèbres. Peut-être s'agit-il d'une
vision prémonitoire ?
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    handle_repas()

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome2/page_9.py", label="9", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
