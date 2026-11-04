import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=368, book=5)

fr_text = """
La hache vous entaille profondément le mollet, vous faisant
hurler de douleur et de surprise. Vous perdez 3 points
d'ENDURANCE. Malgré la douleur, vous attaquez le Garde avant
qu'il ne passe de nouveau à l'attaque et vous réussissez à lui faire
tomber la hache des mains. Le Garde hurle en portant ses doigts
meurtris à la poitrine. Tout en serrant les dents, vous boitillez
vers une porte ouverte. Le grand Palais est en alerte générale et
les bruits de bottes des Gardes et des Drakkars résonnent de
toutes parts. Derrière la porte, un pont enjambe un jardin clos et
relie le Palais à une haute tour en marbre blanc. A l'entrée du
pont, un escalier étroit descend jusqu'au jardin.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-3)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-3)
    st.write_stream(stream_text("Si vous souhaitez traverser le pont pour entrer dans la tour, rendez-vous au :"))
    st.page_link("tomes/tome5/page_396.py", label="396", icon="📄")
    st.write_stream(stream_text("Si vous préférez descendre les marches vers le jardin en contrebas, rendez-vous au :"))
    st.page_link("tomes/tome5/page_215.py", label="215", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
