import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    remove_from_inventory,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=191, book=7)

fr_text = """
Vous tirez la Graine de Feu de votre poche et vous la jetez par
terre. En touchant le sol, elle explose dans un éclair aveuglant et
les serpents s'enfuient de toutes parts en crachant et en sifflant
pour éviter les flammes brûlantes. Soudain, d'autres bruits
retentissent dans la pièce mais, cette fois, ce sont des cliquetis
d'armes et d'armures.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        remove_from_inventory("GRAINE DE FEU")
    st.caption("Vous rayez une Graine de Feu de votre Feuille d'Aventure.")

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_346.py", label="346", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
