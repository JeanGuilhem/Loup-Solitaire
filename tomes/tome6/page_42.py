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

check_inventory(current_page_number=42, book=6)

fr_text = """
A l'intérieur de la tente, un spectacle effroyable et consternant
vous attend: des hommes grièvement blessés gisent à même le sol
boueux ; des pansements de fortune ont été taillés dans leurs
pauvres vêtements, et nombreux sont ceux qui n'ont plus de bottes
aux pieds - probablement à cause des vols commis par des hommes
sans scrupules n'hésitant pas à profiter de la faiblesse et de
l'impuissance de leurs camarades. L'un d'entre eux est justement
en train de couper la bourse d'un soldat inconscient lorsque vous
pénétrez sous la tente. Il se redresse brusquement en vous voyant,
puis il se précipite sur vous en brandissant un poignard à lame
recourbée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("VOLEUR", 16, 21)], flee_after=0)
    if outcome == "fled":
        st.write_stream(stream_text("Si vous désirez prendre la fuite au cours du combat, vous sortez de la tente, puis vous enfourchez votre cheval et vous partez au grand galop. Rendez-vous au :"))
        st.page_link("tomes/tome6/page_70.py", label="70", icon="📄")
    elif outcome == "win":
        st.write_stream(stream_text("Si vous sortez vainqueur du combat, rendez-vous au :"))
        st.page_link("tomes/tome6/page_86.py", label="86", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
