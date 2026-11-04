import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=113, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Avec votre teint clair, votre manteau Kaï et votre tunique, vous
ne passez pas inaperçu au milieu de la foule et vous devez trouver
un endroit pour vous dissimuler. La ruelle se termine par une
place bordée d'arbres. A votre gauche, vous apercevez une petite
demeure dont la curieuse enseigne de bois, accrochée au-dessus
de la porte, évoque la forme d'un poisson. A votre droite, se
trouve une taverne dont le nom inscrit sur l'enseigne semble
étrangement approprié : LE SEIGNEUR POURCHASSÉ.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez pénétrer dans la petite maison, rendez-vous au :"))
    st.page_link("tomes/tome5/page_157.py", label="157", icon="📄")

    st.write_stream(stream_text("Si vous préférez entrer dans la taverne, rendez-vous au :"))
    st.page_link("tomes/tome5/page_188.py", label="188", icon="📄")

    st.write_stream(stream_text("Enfin, si vous maîtrisez la Discipline Kaï de la Guérison, rendez-vous au :"))
    if has_kai("La Guérison"):
        st.page_link("tomes/tome5/page_53.py", label="53", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_53.py", label="53", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
