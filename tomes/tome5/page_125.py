import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=125, book=5)

fr_text = """
Le cheval parcourt quelques mètres puis trébuche sur le quai et
tombe à la mer avec le cadavre de son cavalier. L'équipage a
retiré la passerelle, vous obligeant ainsi à sauter pour franchir le
vide qui vous sépare désormais du navire. Vous sautez un peu
court et vous atterrissez sur la rangée d'avirons qui bordent les
flancs de la galère. Le bois est mouillé et glissant, et vous devez
faire de grands efforts pour pouvoir conserver votre équilibre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous maîtrisez la Discipline Kaï de la Chasse, ajoutez 2 au chiffre obtenu."))
    roll = hazard_roll()
    if roll is not None:
        bonus = 2 if has_kai("La Chasse") else 0
        total = roll + bonus
        if bonus:
            st.write(f"*Chasse : +2, soit un total de {total}.*")
        if total <= 3:
            st.write_stream(stream_text("Si votre total est compris entre 0 et 3, rendez-vous au :"))
            st.page_link("tomes/tome5/page_50.py", label="50", icon="📄")
        else:
            st.write_stream(stream_text("S'il est de 4 ou plus, rendez-vous au :"))
            st.page_link("tomes/tome5/page_191.py", label="191", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
