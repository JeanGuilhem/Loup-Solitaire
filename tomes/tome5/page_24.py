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

check_inventory(current_page_number=24, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
L'homme referme rapidement la porte et en tire le verrou.
Quelques secondes plus tard, vous entendez les pas précipités
des Sharnazims qui pénètrent dans la cour. « Entrez par là »,
chuchote l'homme en désignant du doigt l'intérieur sombre de sa
maison. « Je vais essayer de nous débarrasser des soldats. » Vous
entrez et vous montez l'escalier qui mène à une grande pièce bien
éclairée donnant sur la place du Marché. De longs drapeaux
noirs pendent aux fenêtres du bâtiment situé en face et des
lamentations parviennent à vos oreilles par ses portes grandes
ouvertes.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous maîtrisez la Discipline Kaï du Sixième Sens, rendez-vous au :'))
    if has_kai("Le Sixième Sens"):
        st.page_link("tomes/tome5/page_147.py", label="147", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_147.py", label="147", icon="📄", disabled=True)
    st.write_stream(stream_text('Si vous ne maîtrisez pas cette Discipline, rendez-vous au :'))
    if has_kai("Le Sixième Sens"):
        st.page_link("tomes/tome5/page_196.py", label="196", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome5/page_196.py", label="196", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
