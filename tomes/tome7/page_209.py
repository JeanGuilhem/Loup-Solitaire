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

check_inventory(current_page_number=209, book=7)

fr_text = """
Vous portez le coup de grâce à l'Oudagorg qui recule en se
tordant sur lui-même, la tête dissimulée dans l'épaisseur du
brouillard. Soudain, un éclair jaillit dans un craquement
assourdissant et enveloppe le corps de la créature en crépitant.
Une horrible odeur de chair brûlée se répand dans l'atmosphère
tandis que l'Oudagorg se débat sauvagement. Quelques minutes
après, sa danse macabre cesse, et vous constatez que le voile de
brouillard a disparu. En regardant au-dessus de vous, vous
apercevez alors dans l'obscurité une passerelle déserte et une
plate-forme d'observation en métal noir.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez grimper sur le corps de l'Oudagorg pour vous hisser sur la plate-forme, rendez-vous au :"))
    st.page_link("tomes/tome7/page_294.py", label="294", icon="📄")

    st.write_stream(stream_text("Si vous souhaitez enjamber la carcasse de la créature pour continuer le long du couloir, rendez-vous au :"))
    st.page_link("tomes/tome7/page_46.py", label="46", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
