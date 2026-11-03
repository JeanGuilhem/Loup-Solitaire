import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    lose_backpack,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=158, book=4)

fr_text = """
Votre estomac se retourne lorsque le bateau plonge en avant.
Vous tombez pendant ce qui vous semble une éternité, avant de
heurter tête la première la surface de l'eau. Le choc est tel que
vous êtes assommé sur le coup. Vous perdez aussitôt 3 points
d'ENDURANCE. Lorsque vous reprenez connaissance, vous êtes
étendu à plat ventre sur un sol de boue et de gravier. Le sang
vous bat aux tempes et vous avez l'impression que vos poumons
sont en feu. Vous avez perdu votre Sac à Dos et tout ce qu'il
contenait. Bien que votre vision soit encore trouble, vous vous
apercevez très vite que vous êtes seul. Il n'y a plus trace autour de
vous ni de vos hommes ni du bateau. Apportez les modifications
nécessaires à votre Feuille d'Aventure.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        lose_backpack()
        change_endurance(-3)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-3)
    st.write("*Vous avez perdu votre Sac à Dos et tout son contenu.*")

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_219.py", label="219", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
