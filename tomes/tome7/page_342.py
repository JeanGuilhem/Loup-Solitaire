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

check_inventory(current_page_number=342, book=7)

fr_text = """
La sphère s'arrête à mi-hauteur, à moins de trois mètres de
l'endroit où vous vous trouvez. Elle ressemble à un cerveau
énorme, couvert de grosses verrues poilues. Un sifflement léger
mais terrifiant s'élève, devenant de plus en plus aigu jusqu'à ce
qu'une douleur atroce vous vrille la tête. Vos doigts se mettent à
trembler et vous relâchez votre arme. Une fente s'ouvre soudain
sur le côté du cerveau, et vous apercevez une bouche large et
bouffie aux lèvres pendantes. Une longue vrille de chair en sort et
s'avance en ondulant vers votre gorge.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de l'Écran Psychique, rendez-vous au :"))
    if has_magnakai("Écran Psychique"):
        st.page_link("tomes/tome7/page_217.py", label="217", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome7/page_217.py", label="217", icon="📄", disabled=True)
    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï du Contrôle Animal, rendez-vous au :"))
    if has_magnakai("Contrôle Animal"):
        st.page_link("tomes/tome7/page_35.py", label="35", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome7/page_35.py", label="35", icon="📄", disabled=True)
    st.write_stream(stream_text("Si vous ne maîtrisez aucune de ces Disciplines, rendez-vous au :"))
    st.page_link("tomes/tome7/page_143.py", label="143", icon="📄", disabled=has_magnakai("Écran Psychique") or has_magnakai("Contrôle Animal"))

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
