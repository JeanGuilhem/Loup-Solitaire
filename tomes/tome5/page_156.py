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

check_inventory(current_page_number=156, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Après vous être concentré sur la serrure pendant plusieurs
minutes, vous vous rendez compte qu'elle est reliée à une alarme.
Si vous faites un mauvais numéro, l'alarme se déclenchera,
alertant tous les Gardes du Palais.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous possédez les Disciplines Kaï de la Puissance Psychique et du Sixième Sens, rendez-vous au :'))
    if has_kai("Puissance psychique") and has_kai("Le Sixième Sens"):
        st.page_link("tomes/tome5/page_8.py", label="8", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_8.py", label="8", icon="📄", disabled=True)

    st.write_stream(stream_text('Si vous ne possédez pas ces deux disciplines, rendez-vous au :'))
    if not (has_kai("Puissance psychique") and has_kai("Le Sixième Sens")):
        st.page_link("tomes/tome5/page_98.py", label="98", icon="📄")
    else:
        st.page_link("tomes/tome5/page_98.py", label="98", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
