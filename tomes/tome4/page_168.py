import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=168, book=4)

fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
Vous séparez les deux moitiés de votre Sphère de Feu et vous les
tenez au-dessus de votre tête en reprenant votre marche. Vous
êtes alors saisi d'horreur en apercevant une hideuse créature à la
peau noire perchée sur une poutre, près du plafond. Son regard
diabolique suit chacun de vos mouvements et sa gueule s'ouvre et
se ferme comme si elle proférait de silencieuses malédictions.
Soudain, le monstre s'élance de son perchoir et vous attaque.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous possédez le Glaive de Sommer, rendez-vous au :'))
    if has_item("GLAIVE DE SOMMER"):
        st.page_link("tomes/tome4/page_34.py", label="34", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome4/page_34.py", label="34", icon="📄", disabled=True)

    st.write_stream(stream_text('Sinon, rendez-vous au :'))
    st.page_link("tomes/tome4/page_85.py", label="85", icon="📄", disabled=has_item("GLAIVE DE SOMMER"))

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
