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

check_inventory(current_page_number=149, book=2)

fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
Votre Sixième Sens vous indique que ce garde est un soldat loyal du
royaume de Durenor. Si vous vous mêliez de vouloir le corrompre, il se
sentirait gravement insulté et vous attaquerait aussitôt.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez lui montrer le Sceau d'Hammardal, rendez-vous au :"))
    if has_item("SCEAU D'HAMMARDAL"):
        st.page_link("tomes/tome2/page_223.py", label="223", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome2/page_223.py", label="223", icon="📄", disabled=True)
    st.write_stream(stream_text("Peut-être préférez-vous cependant ne pas lui montrer l'anneau ; peut-être même n'est-il plus en votre possession ; dans ce cas vous pouvez essayer de vous faire passer pour un marchand se rendant à Port Bax en allant au :"))
    st.page_link("tomes/tome2/page_250.py", label="250", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
