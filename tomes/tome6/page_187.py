import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=187, book=6)

fr_text = """
Vous parvenez au dernier moment à éviter la pointe mortelle
d'une lance, mais ne pouvez esquiver un autre coup qui déchire
votre tunique et vous érafle la peau (vous perdez 3 points
d'ENDURANCE). Vous sentez la colère vous gagner et essayez de
dégainer votre arme, mais celle-ci reste coincée dans les sangles
de votre selle. Les gardes s'en aperçoivent et ils se précipitent sur
vous avant que vous puissiez riposter.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-3)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-3)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_22.py", label="22", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
