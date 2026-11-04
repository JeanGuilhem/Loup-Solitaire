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

check_inventory(current_page_number=17, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Vous restez longtemps en proie à la peur et à la nausée, puis vous
continuez à progresser sans faiblir dans l'eau visqueuse, presque
inconscient des dangers qui vous entourent. Finalement, vous
parvenez à un croisement où un tunnel plus large rejoint le vôtre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous désirez poursuivre en prenant le tunnel ouest, rendez-vous au :'))
    st.page_link("tomes/tome5/page_73.py", label="73", icon="📄")
    st.write_stream(stream_text('Si vous préférez tourner vers le nord, en empruntant le nouveau tunnel, rendez-vous au :'))
    st.page_link("tomes/tome5/page_112.py", label="112", icon="📄")
    st.write_stream(stream_text('Si vous voulez plutôt prendre le nouveau tunnel en vous dirigeant vers le sud, rendez-vous au :'))
    st.page_link("tomes/tome5/page_128.py", label="128", icon="📄")
    st.write_stream(stream_text('Si vous maîtrisez la Discipline Kaï du Sixième Sens, rendez-vous au :'))
    if has_kai("Le Sixième Sens"):
        st.page_link("tomes/tome5/page_47.py", label="47", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_47.py", label="47", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
