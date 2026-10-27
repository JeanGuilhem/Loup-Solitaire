import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=143, book=2)

fr_text = """
Vous marchez en direction du sud en suivant le quai et bientôt vous
arrivez à un croisement où une rue mène vers l'est. Toutes les boutiques
de cette rue sont fermées, sauf une, située à votre droite. Une enseigne
est accrochée au-dessus de la porte :
JINELDA KOOP ALCHIMISTE Achat et vente de potions magiques
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez entrer dans cette boutique, rendez-vous au :"))
    st.page_link("tomes/tome2/page_289.py", label="289", icon="📄")
    st.write_stream(stream_text("Si vous préférez poursuivre votre chemin, rendez-vous au :"))
    st.page_link("tomes/tome2/page_186.py", label="186", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
