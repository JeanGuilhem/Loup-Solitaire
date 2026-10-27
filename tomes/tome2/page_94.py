import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=94, book=2)

fr_text = """
Vous insistez auprès du capitaine pour qu'on aille voir ce qui se passe à
bord du bateau, mais il ignore votre demande et ordonne à ses hommes
de poursuivre leurs tâches habituelles. Vous contemplez le navire
marchand qui bientôt disparaît à l'horizon en vous demandant pourquoi
le capitaine a refusé de faire quoi que ce soit, puis vous descendez dans
la coursive et vous vous enfermez dans votre cabine en prenant bien
soin de verrouiller la porte.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_240.py", label="240", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
