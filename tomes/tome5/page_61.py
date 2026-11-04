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

check_inventory(current_page_number=61, book=5)

fr_text = """
Soudain, la porte s'ouvre à la volée et les Sharnazims font
irruption dans la pièce. Vous vous élancez vers la fenêtre, mais
quelqu'un vous saisit par-derrière et vous jette à terre. Vous vous
débattez comme un forcené, mais vous finissez par être maîtrisé,
écrasé par le nombre de vos adversaires. Tandis que l'on vous
traîne dans la cour, vous reconnaissez, l'espace d'une seconde,
l'homme qui vous avait ouvert la porte. Celui-ci sourit d'un air
moqueur en glissant une bourse pleine d'argent dans sa poche...
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_176.py", label="176", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
