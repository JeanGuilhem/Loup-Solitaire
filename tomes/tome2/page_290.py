import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=290, book=2)

fr_text = """
Ce repas sent délicieusement bon et vous vous apprêtez à le dévorer
lorsque vous remarquez soudain, sur le bord de l'assiette, trois gouttes
d'un liquide clair qui vous semble tout d'abord être de l'eau. Mais,
lorsque vous touchez l'une de ces gouttes du bout des doigts, vous vous
apercevez que le liquide est collant et vous reconnaissez aussitôt la
consistance de la sève de gandum, un poison mortel, inodore et
incolore, qui a la faveur des assassins de tout poil. Une fureur soudaine
vous saisit alors et vous vous ruez hors de la chambre avec la ferme
intention de découvrir quel est celui ou celle qui a ainsi tenté de vous
supprimer.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome2/page_200.py", label="200", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
