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

check_inventory(current_page_number=303, book=4)

fr_text = """
Le pont s'écrase contre la paroi. Vos genoux et les jointures de
vos doigts sont douloureusement meurtris, mais vous êtes
toujours vivant et restez agrippé à une planche de la passerelle.
Le choc vous a fait perdre 2 points d'ENDURANCE. Les planches
du pont constituent une excellente échelle que vous vous hâtez
d'escalader pour sortir du puits de mine. Vos ennemis poussent
alors une série de jurons retentissants : ils sont en effet bloqués
de l'autre côté du puits et incapables désormais de vous
poursuivre. Avec un sourire ironique, vous leur faites de la main
un signe d'adieu puis vous pénétrez dans le tunnel orienté à
l'ouest.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-2)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome4/page_348.py", label="348", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
