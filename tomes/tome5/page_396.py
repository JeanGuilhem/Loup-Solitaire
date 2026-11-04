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

check_inventory(current_page_number=396, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
A l'intérieur de la tour de marbre, deux volées de marches se
rejoignent à un palier. Vous entendez des bruits de pas qui
courent au loin. Les bruits se rapprochent. Ils proviennent d'un
des escaliers en colimaçon, mais duquel ? Brusquement, un
groupe de guerriers Drakkars apparaît sur le pont qui mène à la
tour. Vous devez vous échapper sans tarder.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous désirez monter les marches, rendez-vous au :"))
    st.page_link("tomes/tome5/page_322.py", label="322", icon="📄")
    st.write_stream(stream_text("Si vous préférez descendre, rendez-vous au :"))
    st.page_link("tomes/tome5/page_360.py", label="360", icon="📄")
    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï du Sixième Sens, rendez-vous au :"))
    if has_kai("Le Sixième Sens"):
        st.page_link("tomes/tome5/page_266.py", label="266", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_266.py", label="266", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
