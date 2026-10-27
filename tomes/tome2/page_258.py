import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    is_new_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."
check_inventory(current_page_number=258, book=2)

fr_text = """
La puanteur que dégage le navire vous étouffe à demi. Vous perdez 1
point d'ENDURANCE et il vous faut à tout prix vous échapper de cette
cale répugnante où vous finirez par succomber à la pestilence.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-1)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-1)

    st.write_stream(stream_text('Si vous voulez essayer de vous hisser sur le pont, rendez-vous au :'))
    st.page_link("tomes/tome2/page_17.py", label="17", icon="📄")

    st.write_stream(stream_text('Si vous préférez quitter la cale par la porte aménagée dans la cloison opposée, rendez-vous au :'))
    st.page_link("tomes/tome2/page_5.py", label="5", icon="📄")

    st.write_stream(stream_text('Enfin, si vous maîtrisez la Discipline Kaï du Sixième Sens, rendez-vous au :'))
    if has_kai("Le Sixième Sens"):
        st.page_link("tomes/tome2/page_272.py", label="272", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome2/page_272.py", label="272", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
