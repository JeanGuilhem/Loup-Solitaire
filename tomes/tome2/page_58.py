import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    spend_gold,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=58, book=2)

fr_text = """
« Pas de chance, Loup Solitaire, votre stratégie ne manquait pas
d'audace, mais je crois bien que j'ai gagné à présent », déclare bientôt
votre adversaire. Le capitaine avance alors une de ses pièces sculptées
sur le damier et vous vous rendez compte que vous avez perdu. Vous le
félicitez pour sa maîtrise du jeu de Samor et vous lui donnez 10 Pièces
d'Or. « Peut-être voudrez-vous engager une autre partie demain soir ?
demande-t-il, je suis homme à vous offrir une deuxième chance. » «
Peut-être », répondez-vous sans vous avancer. Vous souhaitez bonne
nuit au capitaine qui vous adresse un sourire et vous rejoignez votre
cabine.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if st.session_state.get("visibility_gold_lost", False) is False:
        lost = min(10, st.session_state.purse)
        spend_gold(lost)
        st.session_state["visibility_gold_lost"] = lost
    st.metric(label="Couronnes", value=st.session_state.purse, delta=-st.session_state["visibility_gold_lost"])

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_197.py", label="197", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
