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

check_inventory(current_page_number=274, book=6)

fr_text = """
Vous menez votre cheval adroitement vers l'obstacle que vous
sautez avec facilité. Les cris de colère des gardes se mêlent
maintenant aux acclamations de quelques badauds enchantés du
spectacle. Ils apprécient votre courage et vos talents de
cavalier. Les sentinelles de Quarlen ont la réputation d'avoir une
haute opinion d'eux-mêmes, et quiconque parvient à les ridiculiser
impunément est assuré du soutien et de la faveur des habitants de
la ville. Les clameurs et les jurons s'évanouissent peu à peu
tandis que vous vous enfoncez dans les rues de la ville.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_332.py", label="332", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
