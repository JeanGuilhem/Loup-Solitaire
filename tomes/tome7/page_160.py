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

check_inventory(current_page_number=160, book=7)

fr_text = """
Au moment où le dernier ennemi s'écroule, mort, à vos pieds, un
pan de mur s'ouvre soudain en coulissant, laissant le passage à
un horrible nain barbu, vêtu d'un habit crasseux en velours noir.
Une lueur de malveillance éclaire ses petits yeux porcins tandis
qu'il braque sur votre visage un long tube creux en laiton.
« Faites de beaux rêves ! » l'entendez-vous dire. Aussitôt après, un
jet de vapeur glacial jaillit du tube et vous frappe en pleine figure.
Vous titubez en arrière, toussant et suffoquant tandis que l'âcre
émanation pénètre dans vos poumons. Vous venez d'inhaler un
gaz soporifique très puissant et, le temps que vous réalisiez ce qui
vous arrive, vous sombrez dans un profond sommeil.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_165.py", label="165", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
