import streamlit as st
from combat import combat
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

check_inventory(current_page_number=389, book=5)

fr_text = """
Tandis que vous sautez de la passerelle sur la plateforme
d'atterrissage, la sentinelle fait volte-face, et s'empare de sa
lance. L'homme se tient maintenant entre vous et l'enclos de
l'Itikar et le combat est inévitable.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("SENTINELLE DE LA PLATE-FORME", 15, 23)])
    if outcome == "win":
        st.write_stream(stream_text("Si vous remportez le combat et si vous souhaitez fouiller le corps de la sentinelle, rendez-vous au :"))
        st.page_link("tomes/tome5/page_207.py", label="207", icon="📄")
        st.write_stream(stream_text("Si vous préférez laisser le cadavre et entrer rapidement dans l'enclos de l'Itikar, rendez-vous au :"))
        st.page_link("tomes/tome5/page_224.py", label="224", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
