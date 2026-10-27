import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=255, book=2)

fr_text = """
Vous empoignez votre arme et vous faites une brillante démonstration
de vos talents. Vos maîtres Kaï vous ont enseigné la vitesse et le sens
de l'équilibre, les deux éléments essentiels de la technique du combat.
Et lorsque vous faites tournoyer et virevolter votre arme autour de votre
tête et de votre corps, vos mains bougent avec une telle rapidité qu'on
ne parvient plus à distinguer leurs mouvements : elles se déplacent dans
une sorte de tourbillon indistinct qui semble presque surnaturel. Pour
achever de donner la preuve de votre maîtrise, vous frappez soudain le
bord d'une assiette d'étain que vous envoyez tourbillonner à travers la
salle avec une telle force qu'elle vient se ficher profondément dans la
porte de la cave. L'homme a assisté à tout ce spectacle avec des yeux
ronds de stupeur.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome2/page_268.py", label="268", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
