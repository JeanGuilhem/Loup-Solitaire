import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=136, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Une fois le verrou tiré, vous tournez la poignée, puis vous
entrouvrez la porte de quelques centimètres. Vous apercevez un
escalier qui descend vers une petite pièce où une sentinelle
monte la garde devant une grille en fer. A travers les barreaux,
vous voyez des rangées d'armes et des armures posées sur des
râteliers. Une enseigne est fixée aux barreaux de la grille :
ARMURERIE DU GRAND PALAIS.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï du Camouflage, rendez-vous au :"))
    if has_kai("Le Camouflage"):
        st.page_link("tomes/tome5/page_186.py", label="186", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_186.py", label="186", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous voulez attaquer le Garde, rendez-vous au :"))
    st.page_link("tomes/tome5/page_178.py", label="178", icon="📄")

    st.write_stream(stream_text("Si vous préférez fermer la porte et suivre l'autre passage, rendez-vous au :"))
    st.page_link("tomes/tome5/page_93.py", label="93", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
