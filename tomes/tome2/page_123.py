import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=123, book=2)

fr_text = """
Une étrange énergie anime votre corps. Instinctivement, vous levez le
glaive au-dessus de votre tête et un rayon de soleil vient frapper
l'extrémité de la lame d'où jaillit aussitôt une lumière blanche
aveuglante. Un instant plus tard, cependant, la lumière s'évanouit et
vous sentez peser sur votre épaule la main de Lord Axim. « Venez,
Loup Solitaire, dit-il, il y a encore beaucoup à faire pour préparer votre
retour au Royaume du Sommerlund. » Vous rengainez le glaive dans
son fourreau incrusté de pierreries et vous suivez Lord Axim qui vous
entraîne hors de la chambre du roi.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_40.py", label="40", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
