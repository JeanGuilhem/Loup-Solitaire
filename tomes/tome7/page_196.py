import streamlit as st
from inventory import (
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

check_inventory(current_page_number=196, book=7)

fr_text = """
La flèche siffle vers la sphère mais, au dernier moment, la boule
noire change brusquement de trajectoire, et votre projectile ne
fait que la frôler avant de s'enfoncer dans l'eau du lac. La sphère
menaçante repasse à l'attaque. Vite, vous remettez votre arc en
bandoulière et vous tirez une arme.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez rester sur place pour combattre cet objet, rendez-vous au :"))
    st.page_link("tomes/tome7/page_342.py", label="342", icon="📄")

    st.write_stream(stream_text("Si vous préférez fuir son attaque en vous enfonçant un peu plus dans la fissure, rendez-vous au :"))
    st.page_link("tomes/tome7/page_16.py", label="16", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
