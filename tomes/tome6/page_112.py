import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=112, book=6)

fr_text = """
La créature tressaille, se met à battre l'air avec ses pattes,
puis s'effondre lourdement sur le sol. Son corps s'agite
convulsivement dans un dernier sursaut d'agonie. Vous contemplez
un instant l'ignoble cadavre, mais vous vous en écartez d'un
bond en constatant que sa fourrure grouille de vermine ! Les
infects parasites semblent avoir compris d'instinct que leur
hôte vient de mourir car ils abandonnent immédiatement le corps
afin d'en trouver un autre ! Vous vous dirigez en hâte vers
l'autel pour y remplir votre flacon d'Eau de Taunor. Cette eau
possède des vertus curatives qui vous feront regagner 6 points
d'ENDURANCE. Vous pouvez la boire dès à présent ou bien la
conserver dans votre Sac à Dos pour un usage futur. (Dans ce
cas, n'oubliez pas d'inscrire l'Eau de Taunor sur votre Feuille
d'Aventure.)
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_button("EAU DE TAUNOR", key="taunor", label="Remplir votre flacon d'Eau de Taunor")
    st.caption("Vous pouvez la boire dès maintenant depuis l'onglet Inventaire (6 points d'ENDURANCE).")

    st.write_stream(stream_text("Si vous voulez maintenant inspecter le reste de la chapelle, rendez-vous au :"))
    st.page_link("tomes/tome6/page_24.py", label="24", icon="📄")

    st.write_stream(stream_text("Si vous préférez aller rejoindre Cyrilus sans plus tarder, rendez-vous au :"))
    st.page_link("tomes/tome6/page_338.py", label="338", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
