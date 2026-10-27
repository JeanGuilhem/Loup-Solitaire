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

check_inventory(current_page_number=294, book=2)

fr_text = """
Vous enveloppez l'homme blessé dans une couverture, mais il a déjà
sombré dans un sommeil dont il ne s'éveillera jamais plus. Vous
retournez alors sur le pont où l'on a rassemblé les corps des marins. Le
capitaine Kelman s'approche de vous et vous montre une épée dont la
seule vue donne le frisson. « Cette épée n'est pas celle d'un pirate,
Loup Solitaire, déclare le capitaine, elle a été fabriquée dans les forges
d'Helgedad : c'est une arme de Maître des Ténèbres. » Il jette à la mer
l'épée maléfique qui disparaît dans les vagues et vous revenez tous
deux à bord du Sceptre Vert. L'équipage hisse aussitôt les voiles et le
navire reprend sa route vers l'est tandis que, debout sur le pont, vous
contemplez avec tristesse le bateau de Durenor qui s'enfonce à jamais
dans les flots.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome2/page_240.py", label="240", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
