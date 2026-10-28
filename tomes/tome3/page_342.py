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

check_inventory(current_page_number=342, book=3)

fr_text = """
Votre Discipline Kaï de l'Orientation vous révèle que le tunnel de
droite est orienté à l'est et celui de gauche au nord. Vous vous
trouvez en ce moment juste au-dessous du mont des Brumes.
Consultez la carte de Kalte qui figure au début de ce volume pour
choisir le tunnel que vous allez emprunter.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous prenez le tunnel orienté à l'est, rendez-vous au :"))
    st.page_link("tomes/tome3/page_199.py", label="199", icon="📄")
    st.write_stream(stream_text("Si vous préférez celui qui mène vers le nord, rendez-vous au :"))
    st.page_link("tomes/tome3/page_284.py", label="284", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
