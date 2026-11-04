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

check_inventory(current_page_number=26, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
En examinant la serrure, vous remarquez que celle-ci n'est pas
une serrure ordinaire : une petite plaque de métal bloque le
mécanisme, de telle façon qu'il est impossible de la crocheter.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous possédez la Discipline Kaï de la Maîtrise Psychique de la Matière, rendez-vous au :'))
    if has_kai("Maîtrise Psychique de la Matière"):
        st.page_link("tomes/tome5/page_48.py", label="48", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_48.py", label="48", icon="📄", disabled=True)
    st.write_stream(stream_text('Si vous désirez fracturer la porte, rendez-vous au :'))
    st.page_link("tomes/tome5/page_127.py", label="127", icon="📄")
    st.write_stream(stream_text("Si vous préférez vous éloigner de la porte et vous diriger à présent vers l'autre passage menant à l'escalier, rendez-vous au :"))
    st.page_link("tomes/tome5/page_93.py", label="93", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
