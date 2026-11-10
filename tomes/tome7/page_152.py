import streamlit as st
from inventory import (
    can_shoot,
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=152, book=7)

fr_text = """
Votre flèche atteint sa cible et se plante dans les flancs d'une
autre créature. Cette dernière recule en chancelant et en se
tordant de douleur ; puis elle perd l'équilibre, tombe du pont et
bascule dans le gouffre. Il ne reste maintenant plus qu'une seule
créature indemne sur les trois. Elle s'approche de vous d'un air
menaçant, la gueule encore dégoulinante du sang vert de son
compagnon.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez également lui décocher une flèche, rendez-vous au :"))
    st.page_link("tomes/tome7/page_253.py", label="253", icon="📄", disabled=not can_shoot())

    st.write_stream(stream_text("Si vous préférez faire demi-tour et fuir par le passage opposé, rendez-vous au :"))
    st.page_link("tomes/tome7/page_277.py", label="277", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
