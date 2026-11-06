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

check_inventory(current_page_number=171, book=6)

fr_text = """
L'eau est glaciale ! Elle se referme sur vous comme un étau, vous
coupant le souffle et vous paralysant les bras et les jambes. Au
prix d'un immense effort, vous parvenez à remonter le terrible
courant, et vous atteignez enfin la berge rocheuse. De là, vous
vous traînez jusqu'au déversoir de l'égout.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("A moins que vous ne maîtrisiez la Discipline Magnakaï de Nexus, vous perdez 1 point d'ENDURANCE à cause de ce bain glacé."))
    if has_magnakai("Nexus"):
        st.success("Grâce au Nexus, vous ne souffrez pas du froid.")
    else:
        if is_new_page():
            change_endurance(-1)
        st.metric(label="Endurance", value=st.session_state.endurance, delta=-1)

    st.write_stream(stream_text("A présent, rendez-vous au :"))
    st.page_link("tomes/tome6/page_249.py", label="249", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
