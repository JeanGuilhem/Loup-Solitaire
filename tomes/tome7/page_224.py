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

check_inventory(current_page_number=224, book=7)

fr_text = """
Au moment où votre main saisit la garde de l'épée, la voix du
crâne retentit dans le brouillard au-dessus de vous et vous
écoutez, en frissonnant, les vers suivants :

*Prendre l'arme*

*Rompt un charme*

*Une terreur sèmeras*

*Là où tu iras.*
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez toujours ramasser l'épée, rendez-vous au :"))
    st.page_link("tomes/tome7/page_96.py", label="96", icon="📄")

    st.write_stream(stream_text("Si vous voulez quitter la pièce, sans prendre l'épée, par le tunnel de gauche, rendez-vous au :"))
    st.page_link("tomes/tome7/page_298.py", label="298", icon="📄")

    st.write_stream(stream_text("Si vous préférez partir par le tunnel de droite, rendez-vous au :"))
    st.page_link("tomes/tome7/page_322.py", label="322", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
