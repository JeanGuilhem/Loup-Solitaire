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

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=187, book=3)

fr_text = """
Dès que vous avez refermé le Bracelet autour de votre poignet,
une terrible douleur vous déchire la tête. Vous êtes attaqué par
une puissante Force Mentale qui essaie d'annihiler en vous toute
volonté.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous maîtrisez la Discipline Kaï du Bouclier Psychique, rendez-vous immédiatement au :'))
    if has_kai("Bouclier psychique"):
        st.page_link("tomes/tome3/page_258.py", label="258", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome3/page_258.py", label="258", icon="📄", disabled=True)
    st.write_stream(stream_text('Sinon, rendez-vous au :'))
    st.page_link("tomes/tome3/page_93.py", label="93", icon="📄", disabled=has_kai("Bouclier psychique"))

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
