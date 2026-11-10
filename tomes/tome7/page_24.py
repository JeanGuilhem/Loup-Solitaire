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

check_inventory(current_page_number=24, book=7)

fr_text = """
Après une heure, vous semble-t-il, mais en réalité au bout de
quelques minutes tout au plus, la chaleur torride diminue et l'air
redevient à peu près respirable dans le tunnel. Vous pressez le
pas et vous arrivez bientôt à une arcade ; le couloir d'acier
étincelant débouche sur une pièce qui semble creusée dans un
bloc de fer noir. Là, un escalier en colimaçon grimpe jusqu'à un
portail. Vous y montez, et le spectacle que vous découvrez à
travers ce portail vous coupe le souffle : vous avez devant vous un
énorme bloc d'or massif, le dossier du trône du Seigneur Zahda.
Au-dessus de lui, planant sans bouger dans les airs, il y a deux
cristaux absolument parfaits: l'un d'eux resplendit d'un feu
sombre, l'autre irradie une lumière dorée dont la vue déclenche
en vous une décharge d'adrénaline, c'est l'objet de votre quête, la
Pierre de la Sagesse de Herdos !
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous voulez vous hisser pour atteindre la Pierre de la Sagesse, rendez-vous au :'))
    st.page_link("tomes/tome7/page_42.py", label="42", icon="📄")

    st.write_stream(stream_text("Si vous jugez plus prudent de vous attaquer tout d'abord au cristal noir, rendez-vous au :"))
    st.page_link("tomes/tome7/page_138.py", label="138", icon="📄")

    st.write_stream(stream_text('Si vous préférez examiner le trône avec circonspection, rendez-vous au :'))
    st.page_link("tomes/tome7/page_98.py", label="98", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
