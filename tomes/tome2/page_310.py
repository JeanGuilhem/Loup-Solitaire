import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=310, book=2)

fr_text = """
Vous arrivez bientôt au bout de la rue du Col Vert ; une autre rue
orientée nord-sud la croise à cet endroit, mais il fait si noir à présent
que vous êtes bien incapable de lire le nom qu'elle porte. Il est temps de
trouver un abri pour la nuit et vous apercevez alors, un peu plus loin,
une enseigne éclairée qui indique :
ÉCURIES DE RAGADORN RELAIS DE DILIGENCE
Profitant de l'obscurité, vous montez quatre à quatre une échelle
extérieure qui vous mène à un grenier : c'est l'endroit idéal pour passer
la nuit, blotti parmi des bottes de foin.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_32.py", label="32", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
