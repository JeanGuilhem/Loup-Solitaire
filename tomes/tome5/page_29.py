import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    remove_from_inventory,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=29, book=5)

fr_text = """
Après avoir fait un gros nœud au bout de la corde, vous enroulez
celle-ci autour de votre bras, puis vous lancez l'extrémité nouée
en direction de votre cible. Vous échouez par trois fois. La
quatrième tentative réussit : le nœud se coince entre la barre et le
mur et vous permet de vous hisser hors de l'eau, puis de vous
balancer à travers la voûte pour vous retrouver sans problème
dans le tunnel opposé. Cependant, cette manœuvre vous fait
perdre votre corde, car celle-ci est restée coincée par la barre de
métal et vous n'avez aucun moyen de la décrocher. N'oubliez pas
de rayer cet objet sur votre Feuille d'Aventure. Le souterrain qui
s'ouvre devant vous part en serpentant comme un gigantesque
reptile, et l'air vicié qui flotte autour de vous est chaud et
humide. A présent, bien qu'il semble que vous ayez semé vos
poursuivants, il va falloir vous échapper du Baga-Darooz.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        remove_from_inventory("CORDE")
    st.warning("Vous avez perdu votre Corde.")

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome5/page_55.py", label="55", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
