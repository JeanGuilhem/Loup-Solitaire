import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=58, book=5)

fr_text = """
Vous longez un étroit passage de pierre rose pâle qui se termine
par un vestibule désert. Sur le mur exposé au nord, il y a une
grande porte en bois couverte de plaques de bronze gravées et de
gros clous du même métal. A mi-hauteur se trouve une étrange
serrure encerclée par un long scorpion finement sculpté. En
l'examinant plus attentivement, vous parvenez à déchiffrer une
série de nombres vassagoniens allant de 1 à 200. Vous
reconnaissez immédiatement la nature de ces inscriptions : c'est
une serrure de haute sécurité, à combinaison cloéasienne.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous connaissez le nombre qui déclenche l'ouverture de la porte, rendez-vous au paragraphe portant ce nombre comme numéro."))
    code = st.number_input("Nombre à composer sur la serrure (de 1 à 200)", min_value=1, max_value=200, value=None, step=1, key="code_58")
    if code == 67:
        st.page_link("tomes/tome5/page_67.py", label="67", icon="📄")
    elif code == 76:
        st.page_link("tomes/tome5/page_76.py", label="76", icon="📄")
    elif code is not None:
        st.write("*Ce nombre ne déclenche pas l'ouverture de la porte.*")
    st.write_stream(stream_text("Si vous ignorez le nombre qui commande l'ouverture de la porte, rendez-vous au :"))
    st.page_link("tomes/tome5/page_156.py", label="156", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
