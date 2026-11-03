import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=172, book=4)

fr_text = """
Vous reconnaissez l'accent de l'est. Ce sont des Guerriers Pillards
vassagoniens qui se trouvent de l'autre côté de cette porte. Ils
sont quatre et ils parlent d'un intrus qu'on a repéré dans les
galeries de la mine. Vous estimez qu'en l'occurrence la discrétion
est préférable et vous revenez donc dans le passage. Vous vous
assurez que vous n'êtes pas suivi, puis vous entrez dans le tunnel
orienté à l'ouest et le long duquel sont alignés les chariots.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_55.py", label="55", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
