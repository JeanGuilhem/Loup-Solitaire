import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."
check_inventory(current_page_number=271, book=2)

fr_text = """
Vous entrez dans la tour et vous montez un escalier de pierre ; soudain,
un garde vêtu d'une armure surgit devant vous. Il est coiffé d'un
heaume et il porte un écusson gravé d'un vaisseau noir et d'une crête
rouge. Il s'avance vers vous et tire son épée. « Halte-là ! lance-t-il,
donnez le mot de passe ! »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous maîtrisez la Discipline Kaï du Camouflage, rendez-vous au :'))
    if has_kai("Le Camouflage"):
        st.page_link("tomes/tome2/page_151.py", label="151", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome2/page_151.py", label="151", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous souhaitez l'attaquer, rendez-vous au :"))
    st.page_link("tomes/tome2/page_157.py", label="157", icon="📄")

    st.write_stream(stream_text('Si vous préférez prendre la fuite en vous précipitant hors de la tour, rendez-vous au :'))
    st.page_link("tomes/tome2/page_65.py", label="65", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
