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

check_inventory(current_page_number=32, book=5)

fr_text = """
Après avoir mis le capuchon de votre manteau, vous vous élancez
vers les portes grandes ouvertes et vous pénétrez dans une
immense salle plongée dans la pénombre. A l'intérieur, de
nombreuses personnes sont agenouillées devant une chaire où
un prêtre, vêtu d'une chasuble noir et or, lit à voix haute les
textes d'un livre incrusté de pierreries. Derrière lui, le portrait du
défunt Zakhan, immortalisé sur une tapisserie suspendue au
plafond par de longues cordelettes de soie, domine l'assemblée
en deuil. Abîmées dans leurs prières, les personnes de
l'assistance ne vous voient pas entrer. Bientôt la cérémonie prend
fin et vous pouvez passer au nez et à la barbe des hommes de
Maouk, perdu au milieu du cortège funèbre qui part en
cheminant à travers les rues de la ville.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome5/page_169.py", label="169", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
