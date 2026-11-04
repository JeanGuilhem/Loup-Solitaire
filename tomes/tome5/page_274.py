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

check_inventory(current_page_number=274, book=5)

fr_text = """
Banedon brandit un anneau en argent étincelant sous le nez du
marchand, en lui disant : « Il est à vous, mon ami, si vous me
dites où l'on peut trouver Tipasa. » Le marchand s'empare de
l'anneau puis répond en bredouillant : « Prenez la première allée
après le marché ; Tipasa habite la maison à la porte bleue. » Vous
traversez rapidement la place du marché, pleine de monde à
cette heure-ci, puis vous vous engagez dans la ruelle que l'on
vient de vous indiquer. Soudain, vous entendez un grand cri de
dépit s'élever au-dessus du vacarme de la foule : c'est le
marchand qui manifeste sa déception, car après avoir placé
l'anneau à son doigt, ce dernier s'est littéralement volatilisé ! Au
bout de l'allée, vous apercevez la maison à la porte bleue.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_206.py", label="206", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
