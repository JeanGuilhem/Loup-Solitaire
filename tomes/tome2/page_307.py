import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=307, book=2)

fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
Les soldats se montrent menaçants et prêts à attaquer. Il vous faut
prendre une décision rapide.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez essayer de les corrompre en leur offrant de l'or, rendez-vous au :"))
    st.page_link("tomes/tome2/page_57.py", label="57", icon="📄")
    st.write_stream(stream_text("Si vous préférez leur montrer le Sceau d'Hammardal (en admettant qu'il soit toujours en votre possession), rendez-vous au :"))
    if has_item("SCEAU D'HAMMARDAL"):
        st.page_link("tomes/tome2/page_140.py", label="140", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome2/page_140.py", label="140", icon="📄", disabled=True)
    st.write_stream(stream_text("Si vous estimez enfin qu'il vaut mieux dégainer votre arme et les combattre, rendez-vous au :"))
    st.page_link("tomes/tome2/page_282.py", label="282", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
