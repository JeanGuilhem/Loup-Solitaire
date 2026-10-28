import streamlit as st
from inventory import (
    add_to_inventory,
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=308, book=3)

fr_text = """
En dépit de sa taille, le Casque vous paraît léger et agréable à
porter. Inscrivez-le sur votre Feuille d'Aventure, dans la case
Objets Spéciaux. Chaque fois que vous en serez coiffé au cours
d'un combat, il augmentera de 2 points votre total d'HABILETÉ.
Le couvercle du coffre se referme lentement et vous quittez les
lieux, enchanté de votre trouvaille. Vous poursuivez ensuite votre
chemin le long du couloir et vous montez l'escalier.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page() and not has_item("CASQUE D'ARGENT"):
        add_to_inventory("CASQUE D'ARGENT")
    st.success("*Le Casque d'Argent est rangé dans vos Objets Spéciaux : +2 HABILETÉ au combat.*")
    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome3/page_323.py", label="323", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
