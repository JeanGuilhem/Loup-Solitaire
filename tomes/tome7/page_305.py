import streamlit as st
from inventory import (
    add_to_inventory,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=305, book=7)

fr_text = """
Les motifs sont tissés avec des fils d'or et d'argent, et émaillés de
gemmes et de pierres semi-précieuses. Vous vous émerveillez
devant la beauté de ce véritable travail d'artiste. Ces tapisseries
doivent valoir plusieurs milliers de couronnes ! Une gemme en
particulier attire votre attention : un gros diamant. Incapable de
résister à la tentation, vous vous en emparez et le glissez dans
votre poche. (Notez-le comme Objet Spécial sur votre Feuille
d'Aventure avant de quitter la pièce par la porte.)
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        add_to_inventory("DIAMANT")
    st.info("Le Diamant est inscrit parmi vos Objets Spéciaux.")

    st.write_stream(stream_text("Quittez la pièce par la porte et rendez-vous au :"))
    st.page_link("tomes/tome7/page_256.py", label="256", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
