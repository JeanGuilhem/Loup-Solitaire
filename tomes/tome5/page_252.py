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

check_inventory(current_page_number=252, book=5)

fr_text = """
Vous écartez rapidement vos pieds de la trajectoire du métal
brillant et vous manquez de peu d'être blessé par la hache qui
s'enfonce de plusieurs centimètres dans le sol de pierre polie.
Cependant, avant que le Garde puisse frapper à nouveau, vous
vous précipitez sur lui et, d'un violent coup, vous faites tomber
son arme de ses mains. L'homme pousse un cri en portant ses
doigts brisés à la poitrine. Puis vous faites demi-tour et vous
courez vers une porte ouverte. L'air résonne du bruit des pas
lourds des Gardes du Palais qui sont désormais tous en alerte.
Unis aux Drakkars, ils sont décidés à vous trouver puis à vous
tuer le plus rapidement possible. Derrière la porte, un pont
enjambe un jardin clos, reliant cette partie du Palais à une tour
de marbre blanc, effilée comme une lance. A l'entrée du pont, un
escalier étroit descend vers le jardin en contrebas.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous désirez traverser le pont pour entrer dans la tour, rendez-vous au :"))
    st.page_link("tomes/tome5/page_396.py", label="396", icon="📄")

    st.write_stream(stream_text("Si vous préférez descendre l'escalier pour pénétrer dans le jardin, rendez-vous au :"))
    st.page_link("tomes/tome5/page_215.py", label="215", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
