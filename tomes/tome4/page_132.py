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

check_inventory(current_page_number=132, book=4)

fr_text = """
Vos hommes attachent leurs chevaux puis vous suivent à
l'intérieur de la taverne. Une vieille femme se tient derrière le
bar. Elle a le visage tendu et creusé de rides, comme si elle
souffrait. Elle porte des vêtements d'homme : une chemise et un
pantalon à carreaux. La salle est vide, mais les tables sont
encombrées de chopes de bière encore à moitié pleines.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si cette taverne vous met mal à l'aise, rendez-vous au :"))
    st.page_link("tomes/tome4/page_67.py", label="67", icon="📄")

    st.write_stream(stream_text('Si vous souhaitez poser des questions à la vieille femme, rendez-vous au :'))
    st.page_link("tomes/tome4/page_287.py", label="287", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
