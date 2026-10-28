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

check_inventory(current_page_number=293, book=3)

fr_text = """
Les créatures que vous voyez devant vous sont des Languabarbs,
de cruels et sauvages prédateurs des terres de Kalte. Les
Bakanals constituent leurs proies favorites, et c'est précisément
l'un de ces animaux qu'ils viennent de dévorer, abandonnant ses
restes sur le sol de la caverne. Un autre passage orienté au nord
vous permettrait de poursuivre votre chemin si toutefois vous
parveniez à en atteindre l'entrée : il se trouve en effet tout au
fond de la caverne.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez essayer de passer devant les Languabarbs en espérant qu'ils ne se réveilleront pas, rendez-vous au :"))
    st.page_link("tomes/tome3/page_125.py", label="125", icon="📄")

    st.write_stream(stream_text("Si vous préférez rebrousser chemin et prendre l'autre tunnel, également orienté au nord, rendez-vous au :"))
    st.page_link("tomes/tome3/page_235.py", label="235", icon="📄")

    st.write_stream(stream_text("Enfin, si vous jugez plus judicieux d'attaquer les créatures endormies, rendez-vous au :"))
    st.page_link("tomes/tome3/page_109.py", label="109", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
