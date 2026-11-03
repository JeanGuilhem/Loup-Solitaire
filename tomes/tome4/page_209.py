import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    kai_rank,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=209, book=4)

fr_unknown_rank = "Vous n'avez pas atteint le rang Kaï d'Aspirant."

fr_text = """
D'un coup de lance, votre adversaire vous a projeté en arrière et
vous tombez sur le dos. Tandis que vous vous relevez tant bien
que mal, le cavalier jette sa lance qui vient de se briser et dégaine
un cimeterre. Un sourire maléfique apparaît alors sur son visage
sinistre, découvrant deux rangées de dents noires et pointues. Il
laisse échapper un cri de guerre puis lance son cheval sur vous.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous avez atteint le rang Kaï d'Aspirant (ou un rang supérieur), rendez-vous au :"))
    if kai_rank() >= 6:
        st.page_link("tomes/tome4/page_111.py", label="111", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_rank))
        st.page_link("tomes/tome4/page_111.py", label="111", icon="📄", disabled=True)

    st.write_stream(stream_text('Dans le cas contraire, rendez-vous au :'))
    st.page_link("tomes/tome4/page_43.py", label="43", icon="📄", disabled=kai_rank() >= 6)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
