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

check_inventory(current_page_number=201, book=3)

fr_text = """
La coupe grince au bout des chaînes qui la retiennent et des
débris de pierre tombent du plafond, tandis que vous vous
élancez au-dessus de la crevasse ; vous avez de la chance
cependant, car la Corde tient bon et vous parvenez sans
encombre de l'autre côté. D'un bref mouvement du poignet, vous
détachez la Corde que vous récupérez et vous poursuivez votre
chemin le long du passage. Quelques mètres plus loin, vous
apercevez sur votre droite une porte de pierre en arcade sur
laquelle ont été sculptés d'étranges motifs. Ils représentent des
centaines de squelettes accrochés par groupes de trois ou quatre
à des blocs de pierre aux faces lisses. A côté de la porte se trouve
un levier fixé au mur.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez tirer sur ce levier pour ouvrir la porte, rendez-vous au :"))
    st.page_link("tomes/tome3/page_110.py", label="110", icon="📄")
    st.write_stream(stream_text("Si vous préférez poursuivre votre chemin le long du passage, rendez-vous au :"))
    st.page_link("tomes/tome3/page_63.py", label="63", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
