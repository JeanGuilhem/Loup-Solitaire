import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=158, book=3)

fr_text = """
L'éclaireur Barbare étant à skis, vous ne pourrez livrer contre lui
qu'un seul Assaut ; emporté par son élan, en effet, il passera
devant vous sans s'arrêter, en essayant de vous porter un coup.
Vous devrez alors tenter de le blesser au moment où il arrivera à
votre hauteur.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("ÉCLAIREUR BARBARE", 20, 28)], key="eclaireur", max_rounds=1)
    if outcome is not None:
        last = st.session_state["combat_eclaireur"]["log"][-1]
        if last["ls_loss"] > last["enemy_loss"]:
            st.write_stream(
                stream_text(
                    "Vous avez subi une perte de points d'ENDURANCE supérieure à celle de votre adversaire, "
                    "rendez-vous au :"
                )
            )
            st.page_link("tomes/tome3/page_165.py", label="165", icon="📄")
        elif last["ls_loss"] < last["enemy_loss"]:
            st.write_stream(stream_text("C'est le Barbare qui perd plus de points d'ENDURANCE que vous, rendez-vous au :"))
            st.page_link("tomes/tome3/page_271.py", label="271", icon="📄")
        else:
            st.write_stream(stream_text("Vous perdez tous deux le même nombre de points d'ENDURANCE, rendez-vous au :"))
            st.page_link("tomes/tome3/page_337.py", label="337", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
