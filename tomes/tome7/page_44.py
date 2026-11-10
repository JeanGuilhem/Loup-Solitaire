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

check_inventory(current_page_number=44, book=7)

fr_text = """
Votre main en sang heurte soudain quelque chose près du rebord
du gouffre ; cela ressemble à une étroite passerelle. Vous
bénissez votre chance d'avoir enfin découvert le pont, mais avant
de pouvoir vous y engager, vous recevez un coup dans les côtes
qui vous coupe le souffle. (Vous perdez 3 points d'ENDURANCE.) Le choc vous projette à terre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-3)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-3)

    st.write_stream(stream_text('Si vous voulez vous remettre debout et tenter de riposter, rendez-vous au :'))
    st.page_link("tomes/tome7/page_257.py", label="257", icon="📄")

    st.write_stream(stream_text("Si vous préférez ramper vers le pont invisible et essayer de gagner, tant bien que mal, l'autre côté du gouffre, rendez-vous au :"))
    st.page_link("tomes/tome7/page_166.py", label="166", icon="📄")

    st.write_stream(stream_text('Si vous voulez prendre le risque de sauter dans le vide, rendez-vous au :'))
    st.page_link("tomes/tome7/page_275.py", label="275", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
