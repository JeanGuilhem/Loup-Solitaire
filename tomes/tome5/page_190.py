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

check_inventory(current_page_number=190, book=5)

fr_text = """
Vous avez à peine fait une douzaine de pas que le forgeron vous
aperçoit. L'Armurier géant brandit son lourd marteau et s'avance
vers vous en laissant échapper un grognement sanguinaire. Vous
vous apprêtez à vous défendre, mais vous restez figé sur place un
instant lorsque vous réalisez avec stupeur que son marteau est le
prolongement de son bras droit. Sa main est, en fait, un énorme
poing d'acier. L'Armurier pousse son cri de guerre et vous évitez
de justesse son redoutable bras qui s'écrase violemment contre le
mur en faisant éclater une pierre. Le coup est passé à quelques
centimètres de votre scalp !
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Réduisez de 2 points votre total d'HABILETÉ pour la durée du combat à cause de la chaleur terrible qui règne dans la forge."))
    outcome = combat([("POING D'ACIER L'ARMURIER", 18, 30)], hability_modifier=-2)
    if outcome == "win":
        st.write_stream(stream_text('Si vous remportez le combat, rendez-vous au :'))
        st.page_link("tomes/tome5/page_111.py", label="111", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
