import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=167, book=2)

fr_text = """
«Votre stratégie ne manque pas d'audace, Loup Solitaire, mais je crois
bien que je vais vous battre à présent », lance soudain votre adversaire.
Le capitaine Kelman déplace alors une de ses pièces d'ivoire sculpté de
votre côté du damier en arborant un sourire triomphant. Mais son
sourire s'efface et une expression de contrariété apparaît sur son visage
lorsque vous contre-attaquez d'une manière tout à fait inattendue.
«Échec et mat», répliquez-vous d'une voix calme. Le capitaine
contemple le damier d'un air incrédule. « Décidément, le talent des
Seigneurs Kaï ne cessera jamais de m'étonner », dit-il en se grattant la
tête. Il a toujours les yeux fixés sur le damier du Samor lorsque vous
retournez dans votre cabine après lui avoir souhaité bonne nuit.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_197.py", label="197", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
