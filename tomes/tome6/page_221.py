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

check_inventory(current_page_number=221, book=6)

fr_text = """
Le soldat décroche une torche crépitante du mur puis revient
vers vous. Il la brandit au-dessus de sa tête et, tout en grattant
ses joues mal rasées, vous observe, vous et votre cheval. « D'où
venez-vous ? De Varetta ou de Soren ? De toute façon, vous avez
dû faire un long chemin et vous devez être harassé de fatigue.
Allez, rentrez mais à l'avenir n'oubliez pas votre Pass, les autres
gardes sont moins compréhensifs. » Vous le remerciez, puis vous
franchissez la porte de la ville.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_129.py", label="129", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
