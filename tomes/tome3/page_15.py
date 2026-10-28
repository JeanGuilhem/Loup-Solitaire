import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=15, book=3)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."
fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
Vous examinez attentivement la serrure pour estimer vos
possibilités de la forcer.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            'Si vous possédez la Discipline Kaï de la Maîtrise Psychique de la Matière, rendez-vous '
            'au :'
        )
    )
    if has_kai("Maîtrise Psychique de la Matière"):
        st.page_link("tomes/tome3/page_185.py", label="185", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome3/page_185.py", label="185", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous disposez d'un Poignard ou d'une Épée d'Os, rendez-vous au :"))
    if has_item("POIGNARD") or has_item("ÉPÉE D'OS"):
        st.page_link("tomes/tome3/page_86.py", label="86", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome3/page_86.py", label="86", icon="📄", disabled=True)

    st.write_stream(
        stream_text(
            "Si vous ne maîtrisez pas la Discipline indiquée et que vous n'ayez pas les armes "
            "requises, il vous faut quitter la salle et monter l'escalier en vous rendant au :"
        )
    )
    can_force = has_kai("Maîtrise Psychique de la Matière") or has_item("POIGNARD") or has_item("ÉPÉE D'OS")
    st.page_link("tomes/tome3/page_323.py", label="323", icon="📄", disabled=can_force)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
