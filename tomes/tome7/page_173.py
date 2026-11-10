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

check_inventory(current_page_number=173, book=7)

fr_text = """
Vous continuez à avancer sur la plage malgré vos jambes
endolories, les cris aigus et frénétiques des rats retentissant à vos
oreilles. Derrière un gros bloc de rocher, vous apercevez au fond
d'un ravin encaissé les eaux tumultueuses d'un torrent qui
descend en cascade de la paroi rocheuse surplombant le lac. Un
pont naturel en pierre enjambe le ravin, mais il est très étroit en
son milieu, et vous craignez qu'il ne puisse supporter votre poids.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez traverser l'étroit pont de pierre, rendez-vous au :"))
    st.page_link("tomes/tome7/page_243.py", label="243", icon="📄")

    st.write_stream(stream_text("Si vous préférez essayer de traverser le ravin à la nage, rendez-vous au :"))
    st.page_link("tomes/tome7/page_108.py", label="108", icon="📄")

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de l'Intuition, rendez-vous au :"))
    if has_magnakai("Intuition"):
        st.page_link("tomes/tome7/page_89.py", label="89", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome7/page_89.py", label="89", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
