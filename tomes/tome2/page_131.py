import streamlit as st
from combat import combat
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=131, book=2)

fr_text = """
Vous leur demandez ce qu'ils vous veulent. Pour toute réponse, ils
tirent tous trois d'une poche de leur veste de longs poignards à la lame
recourbée. Leur chef fait alors un pas en avant et vous ordonne de lui
donner votre or. Comme vous hésitez, il crie : « A l'attaque ! » et les
trois VOLEURS bondissent aussitôt sur vous. Il vous faut les affronter un par un.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Vous pouvez prendre la fuite au cours du combat."))
    outcome = combat([("Chef VOLEUR", 15, 23), ("1er VOLEUR", 13, 21), ("2e VOLEUR", 13, 20)], flee_after=0)
    if outcome == "fled":
        st.write_stream(stream_text("Vous prenez la fuite : rendez-vous au :"))
        st.page_link("tomes/tome2/page_121.py", label="121", icon="📄")
    elif outcome == "win":
        st.write_stream(stream_text("Vous avez tué les trois voleurs, rendez-vous au :"))
        st.page_link("tomes/tome2/page_301.py", label="301", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
