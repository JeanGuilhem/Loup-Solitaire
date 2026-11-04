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

check_inventory(current_page_number=163, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Tandis que vous attendez avec anxiété le retour du Garde, l'autre
brute se moque de vous et vous décrit avec délectation les
tortures atroces qui vous attendent. Il est très déçu lorsque
l'autre Garde revient les mains vides. « Le Zakhan ne veut pas
que l'on maltraite notre ami du Nord. Il lui réserve quelque chose
de spécial pour ce soir », grogne-t-il. Puis ils font demi-tour et
s'apprêtent à quitter la cellule, le visage déformé par des
grimaces de haine. A présent, les deux Gardes ont le dos tourné.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez les attaquer, rendez-vous au :'))
    st.page_link("tomes/tome5/page_174.py", label="174", icon="📄")

    st.write_stream(stream_text('Si vous préférez rester dans la cellule, rendez-vous au :'))
    st.page_link("tomes/tome5/page_18.py", label="18", icon="📄")

    st.write_stream(stream_text('Si vous maîtrisez la Discipline Kaï du Sixième Sens, rendez-vous au :'))
    if has_kai("Le Sixième Sens"):
        st.page_link("tomes/tome5/page_144.py", label="144", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_144.py", label="144", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
