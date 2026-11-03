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

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=293, book=4)

fr_text = """
Vous suivez le chemin qui s'enfonce dans les collines boisées.
Bientôt vous découvrez des traces de sabots parfaitement visibles
dans la terre meuble du sentier.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï de l'Orientation, rendez-vous au :"))
    if has_kai("L'Orientation"):
        st.page_link("tomes/tome4/page_18.py", label="18", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome4/page_18.py", label="18", icon="📄", disabled=True)
    st.write_stream(stream_text('Sinon rendez-vous au :'))
    st.page_link("tomes/tome4/page_150.py", label="150", icon="📄", disabled=has_kai("L'Orientation"))

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
