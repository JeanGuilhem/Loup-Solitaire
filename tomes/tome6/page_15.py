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

check_inventory(current_page_number=15, book=6)

fr_text = """
Les gardes de la ville poussent de concert une exclamation de
stupeur, à la fois déconcertés et effrayés par l'aisance avec
laquelle vous venez de neutraliser leur sergent. Ils semblent
hésiter pendant quelques instants puis ils reculent, soucieux
d'éviter votre regard courroucé. D'un léger coup d'éperon, vous
lancez alors votre cheval en direction des chariots, bousculant au
passage une poignée de jeunes recrues qui s'égaient en tous sens
comme des poussins affolés, sans oser vous interpeller. Personne
n'ose se mettre en travers de votre route tandis que vous
manœuvrez habilement autour d'eux avant de partir au grand galop
dans l'allée tortueuse.
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
