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

check_inventory(current_page_number=386, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Quelques mètres au-delà de la place du marché, une ruelle
étroite tourne sur la gauche. Tout au bout, vous apercevez une
maison avec une porte bleu vif.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez prendre cette ruelle et frapper à la porte bleue, rendez-vous au :"))
    st.page_link("tomes/tome5/page_206.py", label="206", icon="📄")
    st.write_stream(stream_text("Si vous désirez continuer le long de la rue où vous vous trouvez, rendez-vous au :"))
    st.page_link("tomes/tome5/page_346.py", label="346", icon="📄")
    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï de l'Orientation, rendez-vous au :"))
    if has_kai("L'Orientation"):
        st.page_link("tomes/tome5/page_292.py", label="292", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_292.py", label="292", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
