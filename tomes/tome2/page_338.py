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
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=338, book=2)

fr_text = """
Vous empoignez la lance et vous la levez au-dessus de votre tête en
visant le Monstre d'Enfer qui se met à hurler de terreur : il sait en effet
que le fer de votre lance lui sera fatal. Sous le choc, vous tombez tous
deux sur la chaussée en contrebas. La chute est rude et vous coûte 2
points d'ENDURANCE. Quant au Monstre d'Enfer, il s'écrase sur la
lance plantée dans sa poitrine et le fer lui transperce instantanément le
cœur.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-2)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)

    st.write_stream(stream_text("Si vous souhaitez arracher votre lance du corps de la créature, rendez-vous au :"))
    st.page_link("tomes/tome2/page_269.py", label="269", icon="📄")
    st.write_stream(stream_text("Si vous préférez abandonner la lance et prendre la fuite aussi vite que possible, rendez-vous au :"))
    if st.button("349 (abandonner la Lance Magique)", key="leave_spear", icon="📄"):
        remove_from_inventory("LANCE MAGIQUE")
        st.switch_page("tomes/tome2/page_349.py")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
