import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, handle_repas, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=5, book=7)

fr_text = """
L'ombre s'embrase brusquement en une gerbe de flammes
rouges avant de se dissoudre en une brume dense et grisâtre
qu'un courant d'air puissant ne tarde pas à disperser. Vous êtes
secoué de frissons. Vous vous enroulez dans votre manteau pour
vous réchauffer, mais le froid qui vous saisit semble plutôt venir
du plus profond de vous-même que de l'atmosphère humide de
l'endroit où vous vous trouvez.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("La faim vous tenaille : vous devez absolument prendre un Repas tout de suite, faute de quoi vous perdrez 3 points d'ENDURANCE."))
    handle_repas()

    st.write_stream(stream_text('Après avoir mangé, vous commencez à avancer prudemment dans la Grande Galerie. Rendez-vous au :'))
    st.page_link("tomes/tome7/page_293.py", label="293", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
