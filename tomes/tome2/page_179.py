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

check_inventory(current_page_number=179, book=2)

fr_text = """
Votre maîtrise du Camouflage vous permet de vous dissimuler dans la
charrette à foin en étant sûr de n'être pas découvert. Lorsque, enfin, tout
danger est écarté, vous sortez de votre cachette.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            "Si, pour plus de sûreté, vous souhaitez rester caché un peu plus longtemps, vous pouvez "
            "vous réfugier au sommet d'une autre meule de foin entassée à quelque distance ; rendez-"
            "vous alors au :"
        )
    )
    st.page_link("tomes/tome2/page_82.py", label="82", icon="📄")

    st.write_stream(stream_text("Si vous préférez prendre un cheval et quitter le village, rendez-vous au :"))
    st.page_link("tomes/tome2/page_150.py", label="150", icon="📄")

    st.write_stream(stream_text("Si enfin vous choisissez d'entrer dans la boutique du charron, rendez-vous au :"))
    st.page_link("tomes/tome2/page_71.py", label="71", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
