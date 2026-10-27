import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=315, book=2)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Tout en gardant un œil sur la porte, vous fouillez rapidement les tiroirs
et les papiers disposés sur une table ouvragée mais vous ne trouvez rien
de suspect. Il n'y a là que des cartes maritimes et des instruments de
navigation. Vous êtes sur le point d'abandonner vos recherches lorsque
vous découvrez un petit levier dissimulé sous la table. Vous l'actionnez
et un panneau glisse aussitôt, révélant une cachette dans laquelle un
petit coffret à la serrure de cuivre a été déposé.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez forcer la serrure de cette boîte, rendez-vous au :"))
    st.page_link("tomes/tome2/page_190.py", label="190", icon="📄")
    st.write_stream(stream_text("Si vous préférez remettre le coffret à sa place et rejoindre le capitaine sur le pont avant qu'il ne soupçonne quelque chose, rendez-vous au :"))
    st.page_link("tomes/tome2/page_175.py", label="175", icon="📄")
    st.write_stream(stream_text("Enfin, si vous possédez la Discipline Kaï de la Maîtrise Psychique de la Matière, rendez-vous au :"))
    if has_kai("Maîtrise Psychique de la Matière"):
        st.page_link("tomes/tome2/page_287.py", label="287", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome2/page_287.py", label="287", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
