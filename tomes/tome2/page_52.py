import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=52, book=2)

fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
Soudain un cri à vous glacer le sang retentit dans l'obscurité, au-dessus
de vous. Vous levez la tête et vous apercevez deux lueurs rougeâtres :
ce sont les yeux d'un Monstre d'Enfer qui descend les marches quatre à
quatre pour se jeter sur vous. Vous hurlez de terreur en cherchant
frénétiquement une arme pour vous défendre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez une Lance Magique, rendez-vous au :"))
    if has_item("LANCE MAGIQUE"):
        st.page_link("tomes/tome2/page_338.py", label="338", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome2/page_338.py", label="338", icon="📄", disabled=True)

    st.write_stream(stream_text("Sinon, rendez-vous au :"))
    st.page_link("tomes/tome2/page_234.py", label="234", icon="📄", disabled=has_item("LANCE MAGIQUE"))

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
