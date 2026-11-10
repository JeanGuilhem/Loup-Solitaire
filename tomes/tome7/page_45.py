import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    completed_lore_circles,
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

check_inventory(current_page_number=45, book=7)

fr_text = """
L'arme au poing, vous vous campez solidement sur vos jambes et
vous vous préparez à affronter la horde grouillante des rats. A
l'air humide de la plage se mêle maintenant la puanteur qui se
dégage du corps des rongeurs qui vous soulève l'estomac. Si vous
avez complété le Cercle de la Lumière (c'est-à-dire si vous
maîtrisez les Disciplines Magnakaï du Contrôle Animal et de la
Science Médicale), vous pouvez ajouter 2 points à votre total
d'HABILETÉ pour toute la durée de ce combat.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat(
        [("HORDE DE RATS GÉANTS", 15, 80)],
        hability_modifier=2 if "Cercle de la Lumière" in completed_lore_circles() else 0,
        flee_after=3,
    )
    if outcome == "fled":
        st.write_stream(stream_text('Vous prenez la fuite en grimpant sur les blocs de rochers. Rendez-vous au :'))
        st.page_link("tomes/tome7/page_336.py", label="336", icon="📄")
    elif outcome == "win":
        st.write_stream(stream_text('Si vous sortez vainqueur du combat, rendez-vous au :'))
        st.page_link("tomes/tome7/page_283.py", label="283", icon="📄")
    elif outcome is None:
        st.caption("Vous pouvez prendre la fuite après 3 Assauts, en grimpant sur les blocs de rochers (rendez-vous alors au 336).")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
