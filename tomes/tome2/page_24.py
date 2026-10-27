import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=24, book=2)

fr_text = """
C'est le tombeau de Killean le Suzerain. Il était l'un des seigneurs de
Ragadorn jusqu'au jour où, trois ans plus tôt, une épidémie de peste
rouge l'emporta en même temps que nombre de ses compatriotes. Vous
vous rappelez soudain les récits que vous a faits un certain Renard
Agile qui occupait un emploi d'artisan au monastère Kaï. Cet homme
s'était souvent rendu à Ragadorn et la peste rouge l'avait frappé tout
comme elle avait frappé une bonne moitié de la population locale.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez retourner dans la taverne, rendez-vous au :"))
    st.page_link("tomes/tome2/page_177.py", label="177", icon="📄")
    st.write_stream(stream_text("Si vous préférez poursuivre votre chemin le long de la rue du Tombeau, rendez-vous au :"))
    st.page_link("tomes/tome2/page_253.py", label="253", icon="📄")
    st.write_stream(stream_text("Si enfin vous désirez prendre la direction de l'est en empruntant la rue de la Tour de Guet, rendez-vous au :"))
    st.page_link("tomes/tome2/page_319.py", label="319", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
