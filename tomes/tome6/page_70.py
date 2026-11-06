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

check_inventory(current_page_number=70, book=6)

fr_text = """
Le sentier se termine à l'endroit où la Storn et la Quarle
convergent en formant un V. Là, des maîtres d'œuvre et des
charpentiers Ogrons s'affairent à construire des pontons en
bois, ressemblant à des barques plates et fermées, qui, une fois
reliés les uns aux autres, formeront un pont flottant destiné à
traverser la rivière en aval. De l'autre côté de la rive, vous
apercevez une tache sombre au ras de l'eau - probablement
l'entrée d'une grotte située juste au pied du mur d'enceinte de
la ville. Mais après avoir mieux examiné l'endroit de votre œil
de lynx, vous distinguez une grille de métal rouillé : ce trou
sombre est en réalité un déversoir d'égout.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous désirez demander à l'un des Ogrons à peau bleue ce qu'il sait au sujet de cette sortie d'égout, rendez-vous au :"))
    st.page_link("tomes/tome6/page_133.py", label="133", icon="📄")

    st.write_stream(stream_text("Si vous voulez tenter de vous emparer d'un ponton afin de traverser la rivière, rendez-vous au :"))
    st.page_link("tomes/tome6/page_163.py", label="163", icon="📄")

    st.write_stream(stream_text("Si vous préférez traverser à la nage, rendez-vous au :"))
    st.page_link("tomes/tome6/page_171.py", label="171", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
