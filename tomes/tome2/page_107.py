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

check_inventory(current_page_number=107, book=2)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Le capitaine donne l'ordre d'aborder le navire marchand et une vision
d'horreur s'offre alors à vous : des cadavres de marins jonchent le pont,
nombre d'entre eux ont le corps percé de flèches et il semble qu'ils ont
dû livrer un combat désespéré pour sauver leur cargaison; les cales du
navire sont vides, cependant, tout a été emporté. En descendant sur le
pont inférieur, vous découvrez le capitaine dans sa cabine ; il est
grièvement blessé et sa fin est proche.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï de la Guérison, rendez-vous au :"))
    if has_kai("La Guérison"):
        st.page_link("tomes/tome2/page_74.py", label="74", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome2/page_74.py", label="74", icon="📄", disabled=True)
        st.write_stream(stream_text("Sinon, rendez-vous au :"))
        st.page_link("tomes/tome2/page_294.py", label="294", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
