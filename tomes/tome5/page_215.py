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

check_inventory(current_page_number=215, book=5)

fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
En bas des marches, une porte en bois consolidée par des barres
de fer donne accès au jardin parfumé. Vous tournez rageusement
la poignée, mais la porte est verrouillée de l'intérieur. Pendant ce
temps, plusieurs Gardes ont surgi sur le pont au-dessus de vous
et, dès qu'ils vous aperçoivent, ils prennent en main leurs lourdes
arbalètes.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez une Clé de Cuivre, rendez-vous au :"))
    if has_item("CLÉ DE CUIVRE"):
        st.page_link("tomes/tome5/page_246.py", label="246", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome5/page_246.py", label="246", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous ne possédez pas cet Objet Spécial, vous pouvez essayer d'escalader la porte. Rendez-vous au :"))
    if has_item("CLÉ DE CUIVRE"):
        st.page_link("tomes/tome5/page_301.py", label="301", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome5/page_301.py", label="301", icon="📄")

    st.write_stream(stream_text("Sinon, vous pouvez remonter l'escalier et courir vers les Gardes le plus rapidement possible avant qu'ils n'aient le temps de charger leurs armes. Rendez-vous au :"))
    st.page_link("tomes/tome5/page_375.py", label="375", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
