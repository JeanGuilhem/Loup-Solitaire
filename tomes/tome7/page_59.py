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
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=59, book=7)

fr_text = """
Au fur et à mesure que vous vous enfoncez dans ce passage,
l'atmosphère devient de plus en plus chaude et résonne d'un
bruit sourd. A moins que vous ne maîtrisiez la Discipline
Magnakaï de Nexus et que vous ayez atteint le rang de Maître
Primat, vous devez dès à présent déduire 3 points de votre total
d'ENDURANCE à cause de la chaleur suffocante et des effluves
sulfureuses qui emplissent le passage. Cependant, à travers le
brouillard jaune, vous distinguez l'entrée d'un autre tunnel sur
votre droite. Les yeux brûlants de larmes, vous scrutez ce
nouveau passage et vous apercevez une lueur rougeâtre
provenant d'une fissure dans le lointain. Le sol, quant à lui, vibre
sous l'effet d'un grincement incessant ; on dirait le frottement
d'objets métalliques sur des pierres et du fer. Ce bruit
horripilant, ajouté à la puanteur de l'atmosphère, ne fait
qu'aggraver votre malaise.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # Nexus au rang de Maître primat : le héros du tome 7 a toujours au moins ce rang
    if has_magnakai("Nexus"):
        st.success("Votre maîtrise de Nexus vous protège de la chaleur et des effluves sulfureuses.")
    else:
        if is_new_page():
            change_endurance(-3)
        st.metric(label="Endurance", value=st.session_state.endurance, delta=-3)

    st.write_stream(stream_text("Si vous voulez aller examiner de plus près la lueur rouge émanant de la fissure, rendez-vous au :"))
    st.page_link("tomes/tome7/page_144.py", label="144", icon="📄")

    st.write_stream(stream_text("Si vous décidez de ne pas vous en occuper et de continuer à remonter rapidement le tunnel où vous vous trouvez, rendez-vous au :"))
    st.page_link("tomes/tome7/page_71.py", label="71", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
