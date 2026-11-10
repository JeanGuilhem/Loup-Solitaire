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

check_inventory(current_page_number=228, book=7)

fr_text = """
Au troisième coup, les blocs de pierre s'effondrent. Sans perdre
de temps, vous vous hissez jusqu'au trou et vous vous retrouvez
de l'autre côté, dans un tunnel humide, creusé de façon
rudimentaire. Le voile de brouillard n'obscurcit plus le plafond,
et vous êtes certain à présent de vous être échappé du labyrinthe.
Le tunnel vire et tourne, tel un gigantesque serpent, jusqu'à ce
que vous arriviez à une palissade. Le bois en est pourri et, après
avoir facilement fait sauter quelques planches, vous continuez à
avancer. Le tunnel de ce côté-ci est beaucoup plus sec et dégagé,
et vous arrivez bientôt à un croisement. Un passage traverse le
tunnel de gauche à droite.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez suivre le passage vers la gauche, rendez-vous au :"))
    st.page_link("tomes/tome7/page_20.py", label="20", icon="📄")

    st.write_stream(stream_text("Si vous préférez suivre le passage vers la droite, rendez-vous au :"))
    st.page_link("tomes/tome7/page_92.py", label="92", icon="📄")

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de l'Exploration, rendez-vous au :"))
    if has_magnakai("Exploration"):
        st.page_link("tomes/tome7/page_330.py", label="330", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome7/page_330.py", label="330", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
