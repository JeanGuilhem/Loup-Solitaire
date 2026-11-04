import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=383, book=5)

fr_text = """
Vous avancez péniblement à travers les dunes de sable orange en
vous couvrant le visage pour vous protéger de la poussière et de
la chaleur brûlante. Le paysage est désolé et hostile; la seule
chose qui semble pouvoir s'y acclimater est une herbe dure
comme du chaume qui griffe vos bottes et vos jambières. Vous
atteignez bientôt le lit d'une rivière asséchée qui mène à une
grotte creusée dans le grès rouge de la colline. Une pancarte en
bois est accrochée au-dessus de l'entrée de la caverne, mais vous
êtes incapable de comprendre les mots étranges peints sur le bois
durci par le soleil.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez examiner la grotte, rendez-vous au :"))
    st.page_link("tomes/tome5/page_235.py", label="235", icon="📄")
    st.write_stream(stream_text("Si vous préférez continuer rapidement votre chemin vers Ikaresh, rendez-vous au :"))
    st.page_link("tomes/tome5/page_272.py", label="272", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
