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

check_inventory(current_page_number=316, book=6)

fr_text = """
Vous vous apprêtez à prendre une chaise pour vous asseoir
lorsque vous sentez la pointe d'un couteau dans votre dos. Votre
sang se fige dans vos veines : un mercenaire a surgi à vos côtés.
« La bourse ou la vie, murmure-t-il à votre oreille. Décide-toi vite,
mon ami n'est pas très patient. »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez donner toutes vos Pièces d'Or sans offrir la moindre résistance, rendez-vous au :"))
    if st.session_state.purse > 0:
        st.page_link("tomes/tome6/page_161.py", label="161", icon="📄")
    else:
        st.page_link("tomes/tome6/page_161.py", label="161", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de l'Art de la Chasse, rendez-vous au :"))
    if has_magnakai("Art de la Chasse"):
        st.page_link("tomes/tome6/page_114.py", label="114", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome6/page_114.py", label="114", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous n'avez pas de Pièces d'Or, ou si vous préférez vous battre avec les voleurs, rendez-vous au :"))
    st.page_link("tomes/tome6/page_282.py", label="282", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
