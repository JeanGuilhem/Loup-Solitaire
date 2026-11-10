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

check_inventory(current_page_number=170, book=7)

fr_text = """
Soudain, il se produit un éclair aveuglant, suivi d'une formidable
explosion. La créature, mise en pièces, se consume en une boule
de feu d'un jaune étincelant. Une vague de chaleur suffocante
vous fouette le visage, vous roussissant la peau et les cheveux
(vous perdez 4 points d'ENDURANCE), puis vous projette dans
les airs. A demi assommé par le choc, vous vous glissez
péniblement à l'intérieur de la fissure maintenant éclairée par les
restes éparpillés du monstre qui se consument lentement sur le
sol.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-4)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-4)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_16.py", label="16", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
