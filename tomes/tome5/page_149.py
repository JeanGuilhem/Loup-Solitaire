import streamlit as st
from inventory import (
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

check_inventory(current_page_number=149, book=5)

fr_text = """
Vous atteignez la porte donnant accès au Vizu-Diar sans être vu,
mais celle-ci est solidement verrouillée de l'intérieur. Vous alliez
maudire votre sort lorsque vous remarquez, au-dessus de la
porte, une fenêtre au cadre finement sculpté et dont les
persiennes de fer sont grandes ouvertes. Malgré votre bras
blessé, vous parvenez à atteindre le rebord de la fenêtre en vous
hissant grâce aux montants cloutés de la porte et vous sautez
dans la Salle des Trophées où règne un inquiétant silence. Une
étrange collection de têtes empaillées borde les murs de cet
endroit très secret. La plupart de ces têtes sont celles de
créatures reptiliennes du désert, souvenir des chasses impériales
dans la Mer de la Sécheresse. Mais, beaucoup plus terrifiantes
que ces trophées de chasse, au milieu des têtes de serpents, se
trouvent des têtes humaines ! Trophées macabres des victoires
des Zakhans, ce sont les têtes des chefs ennemis tués au combat
lors des innombrables guerres menées par la Vassagonie. Vous
quittez rapidement le Vizu-Diar par un long couloir aux murs de
marbre incrusté d'or et de perles qui mène à un grand hall où
vont et viennent les Gardes du Palais et des courtisans aux riches
habits colorés. Dissimulé derrière une rangée de statues, vous
parvenez à atteindre l'escalier qui se trouve au bout du hall sans
être vu. Furtivement, vous grimpez les marches et vous arrivez à
un palier d'où partent deux couloirs ; l'un vers l'est, l'autre vers
l'ouest. Au bout de chaque couloir se trouve une porte au-dessus
de laquelle est gravé un symbole. Au-dessus de la porte est, le
symbole représente un mortier et un pilon. Le symbole de la
porte ouest est un livre ouvert.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez ouvrir la porte est, rendez-vous au :"))
    st.page_link("tomes/tome5/page_57.py", label="57", icon="📄")

    st.write_stream(stream_text("Si vous préférez ouvrir la porte ouest, rendez-vous au :"))
    st.page_link("tomes/tome5/page_100.py", label="100", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
