import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    remove_from_inventory,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=145, book=2)

fr_text = """
Vous vous sentez de plus en plus faible. Au prix d'un effort surhumain,
vous cherchez l'herbe de Laumspur que vous finissez par trouver ; il
vous semble qu'il s'est écoulé une éternité de douleur lorsque vous
parvenez enfin à glisser dans votre bouche quelques feuilles sèches que
vous vous forcez à avaler. Quelques secondes plus tard de violents
malaises convulsent votre corps, puis la douleur s'apaise et vous
sombrez dans un sommeil agité. Il s'écoule presque une heure avant
votre réveil et vous vous sentez encore très mal, si mal que vous perdez
aussitôt 5 points d'ENDURANCE. Peu à peu, cependant, vos forces
reviennent et votre désarroi se change alors en fureur. Vous ramassez
vos affaires et vous quittez la pièce d'un pas chancelant, bien décidé à
retrouver celui ou celle qui a tenté de vous assassiner.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        # les feuilles de Laumspur avalées contre le poison
        if not remove_from_inventory("LAUMSPUR"):
            remove_from_inventory("FIOLE DE LAUMSPUR")
        change_endurance(-5)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-5)
    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_200.py", label="200", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
