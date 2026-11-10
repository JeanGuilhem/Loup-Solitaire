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

check_inventory(current_page_number=120, book=7)

fr_text = """
Le loup bondit sur vous et, ses longues griffes profondément
enfoncées dans votre tunique, il vous envoie rouler à terre avec
lui (vous perdez 4 points d'ENDURANCE). Vous voyez ses crocs
luire à quelques centimètres de votre gorge, et une bave fétide
vous éclabousse le visage pendant que vous vous débattez de
toutes vos forces pour éviter les mortelles mâchoires. Mais
soudain un épouvantable cri retentit. En l'entendant, le loup se
dégage, les yeux fixés avec effroi sur les jets de flammes
ronflantes. A ce moment, une silhouette humaine apparaît ; elle
avance en chancelant et en gémissant. Après avoir poussé un
hurlement sauvage, le loup bat en retraite en voyant approcher le
corps flamboyant qui bat l'air de ses mains et passe à l'attaque.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-4)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-4)

    st.write_stream(stream_text("Si vous voulez vous défendre, rendez-vous au :"))
    st.page_link("tomes/tome7/page_126.py", label="126", icon="📄")

    st.write_stream(stream_text("Si vous préférez contourner cet agresseur enflammé et passer sous les jets de feu, rendez-vous au :"))
    st.page_link("tomes/tome7/page_204.py", label="204", icon="📄")

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
