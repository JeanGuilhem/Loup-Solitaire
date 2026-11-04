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

check_inventory(current_page_number=151, book=5)

fr_text = """
Votre regard, auquel rien n'échappe, tombe sur une étroite
anfractuosité dans le mur du tunnel. Le trou est pratiquement au
niveau de la limite des eaux écumeuses et est à peine visible dans
l'obscurité. Vous vous glissez à l'intérieur, vous faisant le plus
petit possible, tandis que l'eau viciée monte jusqu'à votre
menton. Les Sharnazims passent à quelques centimètres de votre
cachette et vous avez du mal à retenir un vomissement de
dégoût, lorsqu'une éclaboussure vient vous arroser la figure. « Il
a pris le tunnel sud, dit une des voix. Vite, ne perdons pas notre
temps ici ! » Vous avez l'impression que les Sharnazims n'en
finiront jamais de rebrousser chemin le long du tunnel. Avec un
soupir de soulagement, vous vous extirpez de votre niche, mais
vous vous emmêlez les pieds dans quelque chose qui est enfoui
dans la vase du tunnel et vous perdez l'équilibre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome5/page_94.py", label="94", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
