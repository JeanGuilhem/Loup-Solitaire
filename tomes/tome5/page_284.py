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

check_inventory(current_page_number=284, book=5)

fr_text = """
Vous leur criez d'arrêter, mais votre accent vous trahit et
confirme leurs soupçons : vous devez en effet être un espion.
Vous recevez une pierre jetée à toute volée en plein front. Vous
perdez 3 points d'ENDURANCE. « Cours, Loup Solitaire ! crie
Banedon, sinon ils vont te mettre en pièces ! » Peu à peu, les
hommes se rapprochent et vous comprenez à la lueur de férocité
qui brille dans leurs yeux que ce serait folie de rester sur place.
Vous vous retournez donc et vous détalez le plus vite possible.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-3)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-3)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_340.py", label="340", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
