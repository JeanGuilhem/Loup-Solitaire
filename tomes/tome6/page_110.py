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

check_inventory(current_page_number=110, book=6)

fr_text = """
« J'avions point vu personne passer ici, dit la vieille femme
avec l'accent rocailleux des gens de la montagne. L'sentier mène
t'en haut d'ia colline et n'va point plus loin. » Vous sentez
que la femme dit la vérité : le chemin est effectivement sans
issue et nul n'est passé là depuis longtemps. Après avoir
remercié la vieille montagnarde, vous la saluez et vous faites
demi-tour pour redescendre le sentier.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_330.py", label="330", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
