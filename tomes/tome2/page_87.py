import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies, ls_death

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=87, book=2)

fr_text = """
Lorsque vous levez votre arme pour en frapper le chevalier, vous vous
rendez compte trop tard que vous avez commis une erreur fatale, car
l'homme est un escrimeur de toute première force et les soldats
appartiennent au régiment d'élite de la garde du roi Alin IV. Pensant
que vous êtes un Monstre d'Enfer, ils vous encerclent et vous taillent en
pièces. Votre mission s'achève tragiquement en même temps que votre
vie, ici, à Tarnalin.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    show_illustrations()
    ls_death()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
