import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=97, book=2)

fr_text = """
Vous avez remarqué qu'au cours de vos exercices d'entraînement au
maniement du Glaive de Sommer, votre maîtrise de la Discipline Kaï
du Sixième Sens s'est accrue : vous êtes à présent plus sensible que
jamais et vous saviez déjà, bien avant qu'il ait parlé, quelle triste
nouvelle Madin Rendalim allait vous annoncer. Sans nul doute, cette
acuité exceptionnelle de votre Sixième Sens vous sera d'un grand
secours lors de votre voyage de retour à Holmgard.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_152.py", label="152", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
