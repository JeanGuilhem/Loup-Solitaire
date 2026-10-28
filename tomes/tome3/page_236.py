import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=236, book=3)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Dès que le Bracelet d'Or se referme autour de votre poignet, une
douleur fulgurante vous déchire la tête. Vous êtes soumis à
l'attaque d'une puissante Force Mentale qui essaie d'annihiler
votre volonté.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï du Bouclier Psychique, rendez-vous immédiatement au :"))
    if has_kai("Bouclier psychique"):
        st.page_link("tomes/tome3/page_345.py", label="345", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome3/page_345.py", label="345", icon="📄", disabled=True)
    if not has_kai("Bouclier psychique"):
        st.write_stream(stream_text("Sinon, rendez-vous au :"))
        st.page_link("tomes/tome3/page_9.py", label="9", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
