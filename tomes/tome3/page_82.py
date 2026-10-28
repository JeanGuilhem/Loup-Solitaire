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

check_inventory(current_page_number=82, book=3)

fr_text = """
La grotte est sombre et le sol descend en pente raide dans
l'obscurité. Vous parcourez une soixantaine de mètres avant de
distinguer une lueur un peu plus loin. Lorsque vous vous
approchez, vous entendez des bruits, des bruits produits par un
animal.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous maîtrisez la Discipline Kaï de la Communication Animale, rendez-vous au :'))
    if has_kai("Communication Animale"):
        st.page_link("tomes/tome3/page_329.py", label="329", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome3/page_329.py", label="329", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous préférez dégainer votre arme et partir à l'attaque, rendez-vous au :"))
    st.page_link("tomes/tome3/page_138.py", label="138", icon="📄")

    st.write_stream(stream_text('Enfin, si vous jugez plus sage de vous approcher sans bruit pour essayer de voir de quoi il retourne, rendez-vous au :'))
    st.page_link("tomes/tome3/page_107.py", label="107", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
