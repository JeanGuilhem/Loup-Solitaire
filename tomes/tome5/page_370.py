import streamlit as st
from combat import combat
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

check_inventory(current_page_number=370, book=5)

fr_text = """
Vous faites un saut de côté pour éviter les coups de bec mais
l'oiseau vous griffe le dos avec ses puissantes serres et vous
perdez 3 points d'ENDURANCE. Les Itikars sont des créatures
sauvages et féroces de nature. Leur dressage peut prendre
plusieurs années, mais cet effort est toujours largement
récompensé car, une fois domptés, ils demeurent fidèles et
dévoués à leurs maîtres à tout jamais. L'Itikar sent que vous êtes
un étranger et il poursuit son attaque avec acharnement.
Menez ce combat de la façon habituelle, mais multipliez par deux
tous les points d'ENDURANCE perdus par l'oiseau. Lorsque son total d'ENDURANCE sera tombé à zéro, vous l'aurez suffisamment dompté pour pouvoir grimper sur la selle et le
commander. Les blessures qui vous sont infligées vous coûtent le
nombre habituel de points d'ENDURANCE.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-3)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-3)
    outcome = combat([("ITIKAR", 17, 30)], enemy_loss_multiplier=2)
    if outcome == "win":
        st.write_stream(stream_text("Si vous parvenez à réduire le total d'ENDURANCE de l'Itikar à zéro, rendez-vous au :"))
        st.page_link("tomes/tome5/page_217.py", label="217", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
