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

check_inventory(current_page_number=51, book=4)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Vous avez chevauché pendant plus de quatre heures, lorsque
vous apercevez soudain de gros oiseaux noirs qui tournoient au
sommet d'une éminence de terre, un peu plus loin.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez monter sur cette éminence pour l'examiner, rendez-vous au :"))
    st.page_link("tomes/tome4/page_328.py", label="328", icon="📄")

    st.write_stream(stream_text("Si vous préférez ne pas prêter attention à ces oiseaux et poursuivre votre chemin, rendez-vous au :"))
    st.page_link("tomes/tome4/page_120.py", label="120", icon="📄")

    st.write_stream(stream_text("Enfin, si vous maîtrisez la Discipline Kaï de la Communication Animale, rendez-vous au :"))
    if has_kai("Communication Animale"):
        st.page_link("tomes/tome4/page_227.py", label="227", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome4/page_227.py", label="227", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
