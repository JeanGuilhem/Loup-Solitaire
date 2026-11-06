import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=45, book=6)

fr_text = """
Il s'agit d'Altan. Avant même que vous puissiez lui expliquer ce
qui s'est passé, il vous secoue vigoureusement la main en vous
félicitant de votre remarquable adresse. Et il ajoute que, malgré
sa défaite, il se tient prêt à prouver qu'il ne garde aucune
rancune envers vous. Vous le remerciez et vous lui racontez alors
dans quelle fâcheuse situation vous vous trouvez. « Je crois que
nous allons pouvoir nous arranger... » dit-il en regardant votre
Arc en Argent avec convoitise.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez échanger cette arme contre le cheval d'Altan, rendez-vous au :"))
    st.page_link("tomes/tome6/page_212.py", label="212", icon="📄", disabled=not has_item("ARC EN CHÊNE"))

    st.write_stream(stream_text("Si vous ne voulez pas vous défaire de votre Arc en Argent, rendez-vous au :"))
    st.page_link("tomes/tome6/page_148.py", label="148", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
