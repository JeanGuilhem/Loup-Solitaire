import streamlit as st
from combat import combat
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

check_inventory(current_page_number=333, book=4)

fr_text = """
Le cavalier se précipite sur vous au galop. Vous ne pourrez livrer
qu'un seul Assaut car, dans son élan, il sera emporté à plusieurs
mètres de distance après avoir essayé de vous frapper.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("CAVALIER VASSAGONIEN", 20, 28)], key="cavalier", max_rounds=1)
    if outcome is not None:
        last = st.session_state["combat_cavalier"]["log"][-1]
        if last["ls_loss"] > last["enemy_loss"]:
            st.write_stream(stream_text("Si vous perdez plus de points d'ENDURANCE que votre adversaire lors de cet unique Assaut, rendez-vous au :"))
            st.page_link("tomes/tome4/page_209.py", label="209", icon="📄")
        elif last["ls_loss"] < last["enemy_loss"]:
            st.write_stream(stream_text("Si c'est votre ennemi qui perd plus de points d'ENDURANCE que vous à l'issue de l'Assaut, rendez-vous au :"))
            st.page_link("tomes/tome4/page_220.py", label="220", icon="📄")
        else:
            st.write_stream(stream_text("Si vous perdez tous deux le même nombre de points d'ENDURANCE, rendez-vous au :"))
            st.page_link("tomes/tome4/page_344.py", label="344", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
