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

check_inventory(current_page_number=50, book=5)

fr_text = """
Les fines semelles de vos bottes en cuir glissent sur le bois
humide ; vous dérapez et vous tombez à l'eau la tête la première.
Malheureusement, vous heurtez dans votre chute la rangée
d'avirons qui bordent les flancs de la galère et vous perdez 2
points d'ENDURANCE. Les Sharnazims vous repêchent et vous
traînent par le col de votre manteau sur les pavés du quai, puis ils
vous jettent aux pieds de Maouk. Celui-ci vous regarde d'un air
narquois et vous dit : « Vous êtes courageux, Seigneur Kaï, mais
désormais, il va vous falloir plus que du courage pour vous en
tirer ! »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-2)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome5/page_176.py", label="176", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
