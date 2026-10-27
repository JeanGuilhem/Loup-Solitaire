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

check_inventory(current_page_number=174, book=2)

fr_text = """
«Je n'ai encore jamais rencontré un paysan qui ait les moyens de
s'acheter un cheval, dit le chevalier en s'avançant vers vous, vous n'êtes
d'ailleurs sûrement pas un paysan, j'ai plutôt l'impression que vous êtes
un voleur. » Puis, d'un coup de son épée, il vous désarçonne et vous
tombez lourdement sur le sol. Instinctivement, vous tirez votre épée
dans un geste de défense tandis que le chevalier vous attaque.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_162.py", label="162", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
