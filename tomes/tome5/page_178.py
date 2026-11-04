import streamlit as st
from combat import combat
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

check_inventory(current_page_number=178, book=5)

fr_text = """
Vous avez descendu la moitié des marches lorsque le Garde se
rend compte de votre manœuvre. Il dégaine son épée puis se
lance à l'attaque. Vous ne pouvez pas prendre la fuite, et vous
devez vous battre jusqu'à ce que mort s'ensuive.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("GARDE DE L'ARMURERIE", 16, 22)])
    if outcome == "win":
        st.write_stream(stream_text('Si vous remportez le combat, vous pouvez fouiller son cadavre. Rendez-vous en ce cas au :'))
        st.page_link("tomes/tome5/page_52.py", label="52", icon="📄")

        st.write_stream(stream_text("Si vous préférez entrer dans l'Armurerie, sans fouiller le corps, rendez-vous au :"))
        st.page_link("tomes/tome5/page_140.py", label="140", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
