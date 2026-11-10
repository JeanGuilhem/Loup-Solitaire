import streamlit as st
from inventory import (
    can_shoot,
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=104, book=7)

fr_text = """
A moins que vous ne maîtrisiez la Discipline Magnakaï de Nexus,
vous perdez 3 points d'ENDURANCE, le temps d'atteindre la
fissure, car le sable vous a gravement brûlé la plante des pieds.
Debout à l'entrée de la grande lézarde, vous entendez des bruits
suspects s'élever des profondeurs des ténèbres. Mais, pour
l'instant, le danger vient d'un autre côté : une grosse boule noire
et luisante perce soudain la surface du lac ! Dans un sifflement
menaçant, elle fuse vers vous à une vitesse affolante. Qu'allez-
vous faire ?
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # le sable brûlant : 3 points, sauf avec Nexus
    loss = 0 if has_magnakai("Nexus") else 3
    if is_new_page():
        change_endurance(-loss)
    if loss:
        st.metric(label="Endurance", value=st.session_state.endurance, delta=-loss)

    st.write_stream(stream_text("Si vous voulez chercher refuge à l'intérieur de la fissure, rendez-vous au :"))
    st.page_link("tomes/tome7/page_16.py", label="16", icon="📄")

    st.write_stream(stream_text("Si vous préférez dégainer votre arme et vous préparer au combat, rendez-vous au :"))
    st.page_link("tomes/tome7/page_342.py", label="342", icon="📄")

    st.write_stream(stream_text("Si vous possédez un Arc et que vous souhaitiez l'utiliser, rendez-vous au :"))
    st.page_link("tomes/tome7/page_225.py", label="225", icon="📄", disabled=not can_shoot())

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
