import streamlit as st
from combat import combat
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

check_inventory(current_page_number=208, book=6)

fr_text = """
Votre Discipline Magnakaï vous révèle la cachette de l'homme. Il
est accroupi sous un établi à votre droite. Tout à coup, il surgit de
sous la table et vous jette à la figure un flacon en verre mais,
comme vous êtes averti par votre savoir Magnakaï, son attaque
ne vous surprend pas. Vous vous baissez pour éviter le projectile
qui passe en sifflant au-dessus de votre tête avant de s'écraser
contre le mur derrière vous. Le contenu corrosif du flacon
dissout instantanément le plâtre dans un gargouillement sonore.
L'homme dégaine alors une rapière et passe à l'attaque en
poussant d'affreux jurons.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("CHANDA LE TAXIDERMISTE", 17, 24)], flee_after=0)
    if outcome == "fled":
        st.write_stream(stream_text("Vous cessez le combat, sortez du magasin, montez sur votre cheval et partez au galop. Rendez-vous au :"))
        st.page_link("tomes/tome6/page_279.py", label="279", icon="📄")
    elif outcome == "win":
        st.write_stream(stream_text("Si vous remportez le combat, rendez-vous au :"))
        st.page_link("tomes/tome6/page_8.py", label="8", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
