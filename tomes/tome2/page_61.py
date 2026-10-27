import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=61, book=2)

fr_text = """
La pluie tombe si dru qu'il vous est difficile de voir distinctement ;
vous apercevez cependant les silhouettes sombres de gardes en
patrouille qui s'avancent dans votre direction. S'ils vous arrêtaient pour
vous demander ce que vous êtes venu faire à Ragadorn, vous pourriez
bien finir dans l'une des nombreuses geôles de Lachelan le Suzerain. Il
vaut mieux ne pas courir ce risque et vous décidez donc de battre en
retraite le long de la rue du Chevalier Noir et de bifurquer le plus vite
possible dans la rue du Sage ; votre tactique réussit et les gardes passent
sans vous voir.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous à présent au :"))
    st.page_link("tomes/tome2/page_181.py", label="181", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
