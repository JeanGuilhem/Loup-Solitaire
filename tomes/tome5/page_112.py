import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=112, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Vous arrivez bientôt dans une section du tunnel où le plafond est
beaucoup plus haut. A gauche, le long du mur, se trouve une
espèce de trottoir en pierre d'où partent, à intervalles réguliers,
des escaliers. Vous vous hissez sur le trottoir et vous commencez
à enlever la vase qui recouvre vos jambes.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous désirez continuer à avancer en suivant le trottoir, rendez-vous au :"))
    st.page_link("tomes/tome5/page_64.py", label="64", icon="📄")

    st.write_stream(stream_text("Si vous préférez grimper les marches d'un des escaliers à votre gauche, rendez-vous au :"))
    st.page_link("tomes/tome5/page_116.py", label="116", icon="📄")

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï de la Communication Animale, rendez-vous au :"))
    if has_kai("Communication Animale"):
        st.page_link("tomes/tome5/page_133.py", label="133", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_133.py", label="133", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
