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

check_inventory(current_page_number=182, book=3)

fr_text = """
Vous découvrez un étroit passage qui mène à une caverne
hérissée de stalagmites. Deux tunnels s'ouvrent dans la paroi
opposée, tous deux s'enfonçant dans l'obscurité. Des traces
étranges et nombreuses sont visibles dans la neige, à l'entrée de
chaque tunnel.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï de l'Orientation, rendez-vous au :"))
    if has_kai("L'Orientation"):
        st.page_link("tomes/tome3/page_75.py", label="75", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome3/page_75.py", label="75", icon="📄", disabled=True)
    st.write_stream(stream_text('Si vous souhaitez explorer le tunnel de droite, rendez-vous au :'))
    st.page_link("tomes/tome3/page_114.py", label="114", icon="📄")
    st.write_stream(stream_text('Si vous préférez emprunter celui de gauche, rendez-vous au :'))
    st.page_link("tomes/tome3/page_235.py", label="235", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
