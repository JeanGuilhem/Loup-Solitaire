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

check_inventory(current_page_number=59, book=2)

fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
A coups d'éperons, vous lancez votre cheval en direction d'un Monstre
d'Enfer qui s'apprête à frapper un soldat sans défense. Cette créature est
insensible à la Discipline Kaï de la Puissance Psychique et ne peut être
blessée que par une arme magique.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez une Lance Magique, rendez-vous au :"))
    if has_item("LANCE MAGIQUE"):
        st.page_link("tomes/tome2/page_332.py", label="332", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome2/page_332.py", label="332", icon="📄", disabled=True)

    st.write_stream(
        stream_text(
            "Dans le cas contraire, il vous faut prendre la fuite en plongeant dans les broussailles "
            "pour vous y cacher ; rendez-vous alors au :"
        )
    )
    st.page_link("tomes/tome2/page_311.py", label="311", icon="📄", disabled=has_item("LANCE MAGIQUE"))

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
