import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    spend_gold,
)
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=57, book=2)

fr_text = """
Du dos de sa main gantée, l'un des gardes fait sauter de votre paume
l'or que vous lui offrez et les pièces tombent dans les eaux sombres du
chenal de Ryner. Utilisez la Table de Hasard pour savoir combien de
pièces vous avez perdues, en remplaçant le zéro par un 10.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    roll = hazard_roll()
    if roll is not None:
        value = roll if roll != 0 else 10
        if st.session_state.get("visibility_gold_lost", False) is False:
            lost = min(value, st.session_state.purse)
            spend_gold(lost)
            st.session_state["visibility_gold_lost"] = lost
        lost = st.session_state["visibility_gold_lost"]
        st.metric(label="Couronnes", value=st.session_state.purse, delta=-lost)
        st.write_stream(
            stream_text(
                "« Nous n'allons pas vendre la sécurité de notre royaume à si vil prix, dit le garde, "
                "seul un brigand ou un imbécile songerait à corrompre un soldat de Durenor et j'ai bien "
                "l'impression que vous êtes les deux à la fois. » Vous avez eu le tort de porter atteinte "
                "à leur honneur et ils sont en train de vous donner une rude leçon. Rendez-vous au :"
            )
        )
        st.page_link("tomes/tome2/page_282.py", label="282", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
