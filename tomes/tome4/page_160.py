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

check_inventory(current_page_number=160, book=4)

fr_text = """
Une escorte de cinq patrouilleurs vous accompagne le long du
sentier sinueux qui mène à la maison. Il s'agit d'une masure dont
les murs de pierre brute sont recouverts d'une mousse humide.
Elle est dépourvue de fenêtres et l'on y entre par une étrange
porte ovale. Vous avez mis pied à terre et vous vous approchez de
cette porte lorsqu'une voix d'homme à l'intérieur de la masure
lance soudain : « Entrez, Loup Solitaire ! Je vous attendais. »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez pousser la porte et entrer, rendez-vous au :'))
    st.page_link("tomes/tome4/page_84.py", label="84", icon="📄")

    st.write_stream(stream_text("Si vous préférez dégainer votre arme et ouvrir la porte d'un coup de pied, rendez-vous au :"))
    st.page_link("tomes/tome4/page_205.py", label="205", icon="📄")

    st.write_stream(stream_text("Enfin, s'il vous semble plus judicieux d'envoyer quelques-uns de vos hommes dans la maison, rendez-vous au :"))
    st.page_link("tomes/tome4/page_306.py", label="306", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
