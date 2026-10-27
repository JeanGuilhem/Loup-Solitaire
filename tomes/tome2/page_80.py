import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=80, book=2)

fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
Le chevalier remet son épée au fourreau et vous conduit à l'intérieur de
la tour. Vous le suivez le long d'un escalier de pierre qui mène à une
vaste salle ; un feu de bois brûle dans une cheminée en répandant une
agréable chaleur. « Si vous êtes vraiment celui que vous prétendez être,
vous devez avoir en votre possession le Sceau d'Hammardal. Dans ce
cas, montrez-le-moi », ordonne le chevalier.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous acceptez de lui montrer le Sceau, rendez-vous au :"))
    if has_item("SCEAU D'HAMMARDAL"):
        st.page_link("tomes/tome2/page_15.py", label="15", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome2/page_15.py", label="15", icon="📄", disabled=True)

    st.write_stream(
        stream_text(
            "Si vous n'avez plus le Sceau ou si vous ne voulez pas le lui montrer, rendez-vous au :"
        )
    )
    st.page_link("tomes/tome2/page_189.py", label="189", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
