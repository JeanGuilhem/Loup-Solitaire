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

# Les 3 Pièces d'Or du Pass sont payées au paragraphe d'où l'on vient (27 ou 273).

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=304, book=6)

fr_text = """
Le garçon prend rapidement vos Pièces d'Or puis vous tend le
carton bleu et claque la porte. Le carton porte un tampon avec la
date du jour et vous donne accès à la ville d'Amory pour ce jour
seulement. Vous empochez le Pass (inscrivez-le comme Objet
Spécial sur votre Feuille d'Aventure) et vous continuez votre
route.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        add_to_inventory("PASS")
    st.write("*Le Pass a été ajouté à vos Objets Spéciaux.*")

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome6/page_146.py", label="146", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
