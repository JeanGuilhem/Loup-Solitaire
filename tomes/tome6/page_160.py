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

check_inventory(current_page_number=160, book=6)

fr_text = """
Vous empoignez la porte et vous la claquez de toutes vos forces.
Le jeune garçon, pris au dépourvu, la reçoit en pleine figure et
valse à travers la pièce, heurtant au passage une table et une
chaise. Quand le battant s'ouvre à nouveau, après avoir rebondi
sur le chambranle, vous voyez le gamin étendu sur le dos,
inconscient, une grosse bosse sur le front. Sans perdre un
instant, vous ramassez un petit carton bleu et vous constatez
qu'il est daté du jour même. Vous pourrez donc avoir accès à
Amory, mais aujourd'hui seulement. Vous empochez le Pass
(n'oubliez pas de l'inscrire dans la case Objets Spéciaux de votre
Feuille d'Aventure) et vous quittez les lieux avant que le garçon
revienne à lui.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        add_to_inventory("PASS")
    st.success("Vous empochez le Pass (Objet Spécial).")

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_146.py", label="146", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
