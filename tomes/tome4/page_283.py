import streamlit as st
from inventory import (
    change_endurance,
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

check_inventory(current_page_number=283, book=4)

fr_text = """
Vous empoignez le flacon d'Eau Bénite, vous visez soigneusement
et vous le jetez de toutes vos forces. Barraka
s'immobilise, bouche bée, tandis que le flacon vient se fracasser
contre la lame d'acier noir du poignard de Vashna. Une immense
flamme blanche jaillit alors dans un bruit d'explosion. Une
bouffée de chaleur intense vous brûle presque le visage et vous
êtes projeté à terre. Vous perdez 3 points d'ENDURANCE.
Horrifié, vous voyez ensuite Barraka le bras déchiqueté par
l'explosion chanceler en arrière à travers le temple. Il a été
aveuglé par les flammes et sa main valide est crispée sur ses yeux
morts. Dans un silence impressionnant, il trébuche et tombe
dans l'ouverture béante des portes noires aux têtes de morts. Il
est aussitôt précipité au fond des gorges de Maaken et englouti
par le gouffre maudit.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        remove_from_inventory("EAU BÉNITE")
        change_endurance(-3)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-3)
    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_350.py", label="350", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
