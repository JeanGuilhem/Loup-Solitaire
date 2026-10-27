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

check_inventory(current_page_number=134, book=2)

fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
Un cri à vous glacer le sang jaillit tout à coup de l'obscurité et vous
vous retrouvez face à un Monstre d'Enfer aux yeux étincelants. Ses
mains vous attrapent à la gorge et il essaie de vous étrangler; dans un
hurlement de terreur, vous tombez à terre : l'immonde créature déchire
alors votre tunique de ses doigts noirs aux griffes crochues.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez une Lance Magique, rendez-vous au :"))
    if has_item("LANCE MAGIQUE"):
        st.page_link("tomes/tome2/page_38.py", label="38", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome2/page_38.py", label="38", icon="📄", disabled=True)
        st.write_stream(stream_text("Sinon, rendez-vous au :"))
        st.page_link("tomes/tome2/page_304.py", label="304", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
