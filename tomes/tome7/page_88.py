import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    is_new_page,
    show_illustrations,
    show_map,
)
from text import fr_unknown_magnakai
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=88, book=7)

fr_text = """
Des jets de feu jaillissent soudain du sol et des murs, vous
aveuglant momentanément. Une longue flamme vient vous
lécher la figure et vous roussit les cils et les cheveux (vous perdez
2 points d'ENDURANCE). Vous voilà forcé de battre en retraite,
faute de quoi vous finirez grillé vif. Mais soudain, un cri
épouvantable retentit ; quelque chose s'approche de vous à
travers le brasier. La seconde d'après, vous voyez apparaître une
forme humaine auréolée de flammes qui avance en titubant et en
battant l'air de ses bras flamboyants pour vous attaquer.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-2)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)

    st.write_stream(stream_text("Si vous voulez vous préparer à combattre, rendez-vous au :"))
    st.page_link("tomes/tome7/page_126.py", label="126", icon="📄")

    st.write_stream(stream_text("Si vous souhaitez échapper à cet agresseur enflammé en vous élançant dans le brasier infernal, rendez-vous au :"))
    st.page_link("tomes/tome7/page_204.py", label="204", icon="📄")

    st.write_stream(stream_text("Si vous jugez préférable d'éviter l'un et l'autre en remontant le tunnel en sens inverse, rendez-vous au :"))
    st.page_link("tomes/tome7/page_320.py", label="320", icon="📄")

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de Nexus, rendez-vous au :"))
    if has_magnakai("Nexus"):
        st.page_link("tomes/tome7/page_72.py", label="72", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome7/page_72.py", label="72", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
