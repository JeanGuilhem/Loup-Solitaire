import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=347, book=2)

fr_text = """
Au bout de cette rue se trouve une grande écurie. A votre droite, la
populace déchaînée est en train de fouiller les boutiques et les maisons
pour essayer de vous retrouver. Soudain, un homme vous aperçoit et
donne l'alerte. « Il est là ! s'écrie-t-il, c'est lui, c'est l'assassin ! » Vous
n'avez pas le temps de réfléchir : vous vous précipitez à l'intérieur de
l'écurie et vous détachez un cheval ; vous bondissez aussitôt sur sa
croupe et vous filez au galop. Quelqu'un vous lance alors une hache qui
vous atteint à l'épaule en n'occasionnant cependant qu'une simple
égratignure. Vous perdez malgré tout 1 point d'ENDURANCE et vous
disparaissez dans la nuit, loin de vos poursuivants.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-1)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-1)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_150.py", label="150", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
