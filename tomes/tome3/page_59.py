import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=59, book=3)

fr_text = """
Emporté par son élan, le Languabarb continue de charger sur la
mince couche de glace qui cède sous son poids. Sous la surface
gelée, une ombre file alors vers la créature qui se débat
furieusement dans l'eau glacée et l'emporte soudain dans les
profondeurs. Tout devient aussitôt étrangement immobile,
tandis qu'une nappe d'eau rougie s'étale lentement sous la glace.
Vous vous hâtez en direction du tunnel dont les contours
déchiquetés se dessinent de l'autre côté du lac. Lorsque vous
prenez pied sur la glace épaisse de la rive, vous remarquez un
objet à terre. C'est un petit Triangle de Pierre Bleue attaché à une
chaînette.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            "Si vous souhaitez conserver ce Triangle de Pierre Bleue, passez la chaîne autour de votre cou : "
            "il sera rangé dans vos Objets Spéciaux."
        )
    )
    if not has_item("TRIANGLE DE PIERRE BLEUE"):
        pickup_button("TRIANGLE DE PIERRE BLEUE", key="triangle", label="Prendre le Triangle de Pierre Bleue")

    st.write_stream(stream_text('Entrez ensuite dans le tunnel en vous rendant au :'))
    st.page_link("tomes/tome3/page_235.py", label="235", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
