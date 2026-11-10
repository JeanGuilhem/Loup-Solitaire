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

check_inventory(current_page_number=341, book=7)

fr_text = """
Vous êtes couvert du sang du loup que vous venez de tuer, et une
odeur âcre emplit vos narines. L'épée à la main, vous regardez la
dépouille et tremblez à la pensée d'avoir frôlé la mort de si près.
La faible lueur qui baigne les lieux devient soudain plus intense,
et vous entendez un rire froid et distant. L'instant d'après, la
lumière revient à son niveau initial et le rire cesse. Le silence
règne à nouveau.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_298.py", label="298", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
