import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

fr_unknown_item = "Vous ne possédez pas cet objet."

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=92, book=3)

fr_text = """
Vous suivez le passage pendant quelques minutes jusqu'à ce qu'il
tourne vers la gauche ; à votre grande consternation, vous
constatez alors qu'au-delà de cette courbe une fissure s'est
ouverte, provoquant l'écroulement du sol et des murs. Un large
trou noir béant s'ouvre devant vous.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous avez une Corde, rendez-vous au :'))
    if has_item("CORDE"):
        st.page_link("tomes/tome3/page_133.py", label="133", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome3/page_133.py", label="133", icon="📄", disabled=True)

    st.write_stream(stream_text("Dans le cas contraire, vous n'aurez plus qu'à rebrousser chemin pour aller explorer l'autre tunnel. Rendez-vous pour cela au :"))
    st.page_link("tomes/tome3/page_297.py", label="297", icon="📄", disabled=has_item("CORDE"))

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
