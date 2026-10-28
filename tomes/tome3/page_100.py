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

check_inventory(current_page_number=100, book=3)

fr_text = """
Le traître bossu laisse échapper un cri de surprise en vous voyant
soudain apparaître devant lui, mais il se reprend bientôt et se
précipite vers une porte aménagée dans le mur du fond. Les
Barbares des Glaces tirent leur épée ; leurs mouvements,
cependant, sont lents et incertains. Vous parvenez à les
repousser avant qu'ils n'aient pu vous porter le moindre coup, et
vous vous lancez à la poursuite du mage qui s'enfuit. La porte par
laquelle il s'est éclipsé ouvre sur un palier d'où partent deux
escaliers. A votre droite, un escalier en colimaçon descend vers
des étages inférieurs ; à votre gauche, une volée de marches monte
vers une arcade. Il n'y a aucune trace de Vonotar alentour.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez descendre l'escalier en colimaçon, rendez-vous au :"))
    st.page_link("tomes/tome3/page_148.py", label="148", icon="📄")

    st.write_stream(stream_text("Si vous préférez monter les marches qui mènent à l'arcade, rendez-vous au :"))
    st.page_link("tomes/tome3/page_61.py", label="61", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
