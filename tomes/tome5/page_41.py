import streamlit as st
from inventory import (
    check_inventory,
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

check_inventory(current_page_number=41, book=5)

fr_text = """
Vous prenez une gorgée d'huile, mais vous n'arrivez pas à l'avaler
car elle est absolument infecte. Vous la recrachez et buvez un bon
demi-litre d'eau pour vous débarrasser du goût immonde.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez maintenant vous frictionner la peau avec l'huile, rendez-vous au :"))
    st.page_link("tomes/tome5/page_103.py", label="103", icon="📄")
    st.write_stream(stream_text('Si vous préférez ne plus vous occuper de cette huile, rendez-vous au :'))
    st.page_link("tomes/tome5/page_71.py", label="71", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
