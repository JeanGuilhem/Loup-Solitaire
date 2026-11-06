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

check_inventory(current_page_number=55, book=6)

fr_text = """
« Peuh ! s'écrie l'un des gardes avec mépris. Nous n'avons pas
besoin d'étrangers stupides. Retournez à Casiorn si vous n'avez
rien à faire ici ! » Sur ces mots, il crache par terre et va
rejoindre ses compagnons du côté de la porte grande ouverte.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez tenter de soudoyer les gardes afin qu'ils vous laissent passer, rendez-vous au :"))
    st.page_link("tomes/tome6/page_9.py", label="9", icon="📄")

    st.write_stream(stream_text("Si vous désirez profiter du fait que la porte est restée ouverte pour contourner les gardes et entrer de force dans la ville, rendez-vous au :"))
    st.page_link("tomes/tome6/page_261.py", label="261", icon="📄")

    st.write_stream(stream_text("Si vous préférez tourner bride pour aller tenter votre chance à la porte nord de la cité, rendez-vous au :"))
    st.page_link("tomes/tome6/page_137.py", label="137", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
