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

check_inventory(current_page_number=143, book=5)

fr_text = """
Vous allumez une torche enduite de goudron puis vous la jetez
dans la bouche d'égout. L'explosion se produit aussitôt : un
énorme grondement accompagne un éclair aveuglant et les
immondices enflammés jaillissent des profondeurs du Baga-Darooz.
La foule affolée s'enfuit en hurlant dans la rue en
essayant d'éviter les matières en flamme qui pleuvent sur leurs
têtes. En effet, la torche a provoqué une réaction en chaîne dans
le Baga-Darooz. Les gaz des égouts, très inflammables, ont pris
brusquement feu, semant partout la panique et la confusion.
Vous courez dans la rue semée d'immondices et vous suivez la
foule jusqu'à une place où se tient un marché très animé, hors
d'atteinte de la pollution créée par l'explosion. Votre regard est
attiré par une enseigne suspendue au-dessus de la porte latérale
d'un grand bâtiment. Vous pouvez y lire : BAINS PUBLICS DE
BARRAKEESH. Vous poussez la porte et vous vous glissez à
l'intérieur du bâtiment.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_90.py", label="90", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
