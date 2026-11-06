import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    remove_from_inventory,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=49, book=6)

fr_text = """
Le garde vous arrache le petit carton bleu des mains, puis il va
l'examiner à la lumière d'une torche fumante accrochée au mur. Il
enlève ensuite le flambeau de son support et revient vers vous,
approchant la flamme de votre visage pour mieux observer vos
traits. « Passez ! » finit-il par maugréer, tout en froissant la
carte dans sa main velue. D'un coup de talon, vous éperonnez votre
cheval épuisé et vous vous engagez sous la porte de la ville.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # le garde garde le Pass (acheté au 304)
    if is_new_page():
        remove_from_inventory("PASS")

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_129.py", label="129", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
