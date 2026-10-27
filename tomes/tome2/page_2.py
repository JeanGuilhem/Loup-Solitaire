import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=2, book=2)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Vous suivez une route étroite et sinueuse, le long de la côte. De hautes
falaises en surplomb se dressent sur un côté du chemin. A quelque
distance, un éboulement interdit le passage et il vous faut vous arrêter
pour dégager la voie. Mais, alors que vous aidez le conducteur à
soulever un énorme rocher en vous servant d'un levier, vous en
entendez tomber un autre et, un instant plus tard, une gigantesque
masse de pierre se fracasse sur la chaussée, écrasant le conducteur sous
son poids. L'homme est tué sur le coup avant que vous ayez pu faire le
moindre geste pour essayer de le sauver. Le rocher est tombé du haut
de la falaise et vous avez bien failli vous-même le recevoir sur la tête,
car le malheureux qui vient de périr ne se trouvait qu'à deux mètres de
vous.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï du Sixième Sens, rendez-vous au :"))
    if has_kai("Le Sixième Sens"):
        st.page_link("tomes/tome2/page_42.py", label="42", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome2/page_42.py", label="42", icon="📄", disabled=True)
    st.write_stream(stream_text("Dans le cas contraire, rendez-vous au :"))
    st.page_link("tomes/tome2/page_168.py", label="168", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
