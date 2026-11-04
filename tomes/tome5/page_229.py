import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    is_new_page,
    remove_from_inventory,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=229, book=5)

fr_text = """
Alors que le vaisseau apparaît dans la lumière du soleil, un
terrible bruit retentit : le vrombissement strident des Kraans qui
se laissent tomber en piqué de leurs pitons rocheux. Avant
l'aube, leurs cavaliers connaissaient déjà votre cachette avec
certitude et ils ont attendu patiemment sur leur perchoir que
vous passiez avant de tendre leur embuscade. Le Cube de Cristal
noir leur a permis de suivre votre évasion à travers les monts du
Dahir comme si votre route était éclairée par des flambeaux.
Comprenant que ce Cube vous a trahi, vous le sortez rapidement
de votre poche, mais avant même que vous n'ayez pu le jeter au
loin, celui-ci explose dans votre main.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        remove_from_inventory("CUBE DE CRISTAL NOIR")

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous maîtrisez la Discipline Kaï du Sixième Sens, ajoutez 3 au chiffre obtenu."))
    roll = hazard_roll()
    if roll is not None:
        bonus = 3 if has_kai("Le Sixième Sens") else 0
        total = roll + bonus
        if bonus:
            st.write(f"*Bonus : +{bonus}, soit un total de {total}.*")
        if total <= 6:
            st.write_stream(stream_text("Si votre total est compris entre 0 et 6, rendez-vous au :"))
            st.page_link("tomes/tome5/page_385.py", label="385", icon="📄")
        else:
            st.write_stream(stream_text("Si votre total est compris entre 7 et 12, rendez-vous au :"))
            st.page_link("tomes/tome5/page_251.py", label="251", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
