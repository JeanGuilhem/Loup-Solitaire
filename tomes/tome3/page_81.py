import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=81, book=3)

fr_text = """
Vous vous apprêtez à cacher le cadavre sous l'escalier lorsque
vous entendez soudain d'étranges cris et des hurlements rauques
qui viennent du couloir. Un groupe de Barbares des Glaces
s'avance vers vous. La vue de ces guerriers vous laisse un instant
bouche bée : ce sont en effet de hideux mutants. Rempli de
crainte et de dégoût, vous montez l'escalier quatre à quatre
jusqu'à un vaste palier où vous trouvez un couloir orienté nord-
sud.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez courir en direction du nord, rendez-vous au :'))
    st.page_link("tomes/tome3/page_198.py", label="198", icon="📄")

    st.write_stream(stream_text('Si vous préférez aller vers le sud, rendez-vous au :'))
    st.page_link("tomes/tome3/page_69.py", label="69", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
