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

check_inventory(current_page_number=21, book=4)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Au bout d'une demi-heure, l'un de vos hommes déclare avoir
repéré un sentier un peu plus loin. Ce chemin étroit et couvert de
poussière est orienté est-ouest.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez le suivre en direction de l'est, rendez-vous au :"))
    st.page_link("tomes/tome4/page_134.py", label="134", icon="📄")

    st.write_stream(stream_text("Si vous préférez l'emprunter en direction de l'ouest, rendez-vous au :"))
    st.page_link("tomes/tome4/page_191.py", label="191", icon="📄")

    st.write_stream(stream_text("Enfin, si vous maîtrisez la Discipline Kaï de l'Orientation, rendez-vous au :"))
    if has_kai("L'Orientation"):
        st.page_link("tomes/tome4/page_264.py", label="264", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome4/page_264.py", label="264", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
