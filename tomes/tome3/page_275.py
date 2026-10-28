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

check_inventory(current_page_number=275, book=3)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Le tunnel, étroit et bas de plafond, descend en pente douce vers
une caverne d'où jaillit une lumière. Lorsque vous arrivez au
bout du passage, vous jetez un regard prudent à l'intérieur de
cette grotte, de peur que votre arrivée ne dérange quelqu'un ou
quelque chose qu'il vaudrait mieux laisser tranquille. Vous avez
eu raison d'être prudent car deux grandes créatures à l'épaisse
fourrure sont couchées au milieu de cet espace glacé. Les débris
d'une carcasse déchiquetée sont répandus sur la neige autour des
deux énormes bêtes.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï de la Chasse, celle de l'Orientation ou celle de la Communication Animale, rendez-vous au :"))
    if has_kai("La Chasse") or has_kai("L'Orientation") or has_kai("Communication Animale"):
        st.page_link("tomes/tome3/page_293.py", label="293", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome3/page_293.py", label="293", icon="📄", disabled=True)
        st.write_stream(stream_text("Sinon, rendez-vous au :"))
        st.page_link("tomes/tome3/page_197.py", label="197", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
