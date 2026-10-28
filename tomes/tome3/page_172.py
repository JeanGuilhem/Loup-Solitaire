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

check_inventory(current_page_number=172, book=3)

fr_text = """
Vous refusez l'huile de Bakanal que vous propose Irian et vous
retournez sous la tente. Les autres, cependant, après vous avoir
félicité de votre victoire sur la créature, sortent à leur tour de la
tente et vont rejoindre Irian. Stupéfait, vous les voyez alors
plonger eux aussi les mains dans la graisse de Bakanal et s'en
enduire le corps sous leurs vêtements. Un peu plus tard dans la
soirée, vous finissez par vous endormir, non sans avoir pris la
précaution de vous boucher les narines avec du coton. Les autres,
pour leur part, ne semblent pas le moins du monde incommodés
par l'épouvantable odeur.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome3/page_134.py", label="134", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
