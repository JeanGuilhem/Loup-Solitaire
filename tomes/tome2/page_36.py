import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    has_kai,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=36, book=2)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."
fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
Cette nourriture vous semble délicieuse et en quelques minutes, vous
avez vidé votre assiette. Vous décidez alors de faire un petit somme
avant d'aller rejoindre les autres au bar. Mais comme vous vous
apprêtez à vous étendre, une terrible douleur vous tord soudain
l'estomac. Vos jambes se dérobent et vous vous écroulez sur le sol, le
corps saisi de tremblements. Vous avez l'impression qu'un feu vous
brûle tout entier. Un mot vous revient sans cesse à l'esprit, tournant
dans votre tête d'une manière lancinante: poison... poison... poison...
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous avez de l'herbe de Laumspur avec vous, rendez-vous au :"))
    if has_item("LAUMSPUR") or has_item("MOISSON DE LAUMSPUR"):
        st.page_link("tomes/tome2/page_145.py", label="145", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome2/page_145.py", label="145", icon="📄", disabled=True)
    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï de la Guérison, rendez-vous au :"))
    if has_kai("La Guérison"):
        st.page_link("tomes/tome2/page_210.py", label="210", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome2/page_210.py", label="210", icon="📄", disabled=True)
    st.write_stream(stream_text("Si vous n'avez ni l'un ni l'autre, rendez-vous au :"))
    st.page_link("tomes/tome2/page_275.py", label="275", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
