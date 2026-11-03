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

check_inventory(current_page_number=24, book=4)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Vous sautez par-dessus le corps du Guerrier mort et vous
pénétrez dans la tour de guet. Montant quatre à quatre le large
escalier de pierre, vous atteignez un palier au premier étage où
deux soldats tirent des flèches à travers des meurtrières.
Soudain, l'un d'eux pousse un cri de douleur et recule en
chancelant, une flèche enfoncée dans la poitrine.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï de la Guérison, vous pouvez venir en aide à ce soldat blessé en vous rendant au :"))
    if has_kai("La Guérison"):
        st.page_link("tomes/tome4/page_238.py", label="238", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome4/page_238.py", label="238", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous souhaitez continuer à monter les marches jusqu'au sommet de la tour, rendez-vous au :"))
    st.page_link("tomes/tome4/page_223.py", label="223", icon="📄")

    st.write_stream(stream_text("Si vous préférez ramasser l'arc du soldat blessé et prendre sa place derrière la meurtrière, rendez-vous au :"))
    st.page_link("tomes/tome4/page_207.py", label="207", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
