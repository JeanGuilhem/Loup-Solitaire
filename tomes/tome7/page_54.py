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

check_inventory(current_page_number=54, book=7)

fr_text = """
Votre sensibilité de Maître Kaï vous permet d'identifier la nature
de la serrure : il ne s'agit pas d'un simple mécanisme, mais d'un
système de fermeture magique.
Ce n'est pas la peine d'essayer d'en percer le secret, le sortilège
qui bloque la porte résistera à toute tentative de votre part. Vous
abandonnez donc la porte à contrecœur et vous sortez de la pièce
en empruntant l'escalier.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_193.py", label="193", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
