import streamlit as st
from inventory import (
    add_to_inventory,
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    is_new_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=263, book=2)

fr_text = """
L'homme contemple le Sceau avec une stupeur mêlée de crainte. Sans
dire un mot, il se lève alors de son fauteuil et vous fait signe de le
suivre en haut d'un escalier qui mène à une pièce en forme de dôme.
Vous y rencontrez le capitaine de la Tour de Guet qui vous écoute
attentivement tandis que vous lui faites le récit des événements qui sont
survenus au royaume du Sommerlund. Vous lui révélez également le
but de votre mission. « Donnez immédiatement à cet homme un
laissez-passer rouge ! Priorité absolue ! » ordonne-t-il aussitôt. Vous
prenez votre laissez-passer, vous quittez la tour et vous vous hâtez en
direction du poste de garde.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page() and not has_item("LAISSEZ-PASSER ROUGE"):
        add_to_inventory("LAISSEZ-PASSER ROUGE")
    st.success("Le Laissez-passer rouge est ajouté à vos Objets Spéciaux.")

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome2/page_246.py", label="246", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
