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

check_inventory(current_page_number=329, book=5)

fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
Le lourd tambour de cuivre bascule de son socle en bois et dévale
l'escalier de la tour en roulant sur lui-même. Un grondement
grandissant retentit dans les ténèbres au fur et à mesure qu'il
poursuit sa course en direction de vos poursuivants. Au moment
de la collision, les cris d'horreur qui s'élèvent ne sont que de
courte durée, car les Drakkars sont littéralement écrasés au
passage du gigantesque instrument. La rapidité de votre action
vous a permis de vous débarrasser de vos ennemis, mais la
victoire est amère : vous découvrez que vous êtes pris au piège,
car il n'y a pas d'autre issue qui vous permette de vous évader de
la plate-forme. Par ailleurs, vous ne bénéficiez que d'un court
répit et vous devez à nouveau prendre une décision rapide.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous possédez une Corde, vous pouvez essayer de descendre le long de la tour, dans les jardins en contrebas. Rendez-vous au :'))
    if has_item("CORDE"):
        st.page_link("tomes/tome5/page_305.py", label="305", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome5/page_305.py", label="305", icon="📄", disabled=True)

    st.write_stream(stream_text('Si vous ne possédez pas de Corde, rendez-vous au :'))
    if has_item("CORDE"):
        st.page_link("tomes/tome5/page_387.py", label="387", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome5/page_387.py", label="387", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
