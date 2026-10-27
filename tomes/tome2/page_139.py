import streamlit as st
from inventory import (
    add_to_inventory,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=139, book=2)

fr_text = """
L'entraînement que vous avez suivi dans l'art de la chasse vous permet
de reconnaître les fruits comestibles ou vénéneux qui poussent dans les
régions septentrionales de Magnamund. Ces fruits violets sont des
Larnumes. C'est là un mets de choix, sucré et nourrissant. Vous en
mangez à satiété et vous en faites provision pour l'équivalent de 2
repas. Conservez-les dans votre Sac à Dos. Au-delà des larnumiers, les
arbres qui portent ces fruits, vous distinguez une large route qui suit la
côte en menant, au choix, vers l'est ou vers l'ouest.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        add_to_inventory("REPAS", quantity=2)
    st.write_stream(stream_text("Si vous voulez aller vers l'est, rendez-vous au :"))
    st.page_link("tomes/tome2/page_27.py", label="27", icon="📄")
    st.write_stream(stream_text("Si vous préférez prendre la direction de l'ouest, rendez-vous au :"))
    st.page_link("tomes/tome2/page_114.py", label="114", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
