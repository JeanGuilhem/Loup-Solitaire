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

check_inventory(current_page_number=69, book=3)

fr_text = """
Vous avez parcouru moins d'une vingtaine de mètres lorsque
vous voyez soudain apparaître une patrouille de six Barbares des
Glaces qui marchent dans votre direction, le long du couloir.
Vous remarquez alors, sur votre gauche, un petit escalier qui
descend dans une salle obscure.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez courir au bas de ces marches pour vous cacher de la patrouille, rendez-vous au :'))
    st.page_link("tomes/tome3/page_108.py", label="108", icon="📄")

    st.write_stream(stream_text('Si vous souhaitez battre en retraite vers le palier et prendre le couloir orienté au nord, rendez-vous au :'))
    st.page_link("tomes/tome3/page_198.py", label="198", icon="📄")

    st.write_stream(stream_text('Enfin, si vous maîtrisez la Discipline Kaï du Camouflage, rendez-vous au :'))
    if has_kai("Le Camouflage"):
        st.page_link("tomes/tome3/page_222.py", label="222", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome3/page_222.py", label="222", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
