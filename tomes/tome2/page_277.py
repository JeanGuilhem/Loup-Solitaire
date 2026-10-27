import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=277, book=2)

fr_text = """
Tandis que Rhygar et ses hommes se rapprochent des cavaliers, l'un
d'eux tire de sous sa cape un bâton noir. Une flamme bleue étincelante
jaillit alors de son extrémité et vient frapper le cheval du Lieutenant
Général qui est aussitôt projeté à bas de sa monture et tombe cul par-
dessus tête dans l'épaisseur des broussailles. Les hommes de Rhygar se
lancent à l'attaque, leurs épées brandies, et pourfendent les cavaliers
aux longues capes. Mais les lames d'acier n'ont aucun effet sur
l'ennemi, car ce ne sont pas des hommes que vous avez devant vous, ce
sont des Monstres d'Enfer, les féroces serviteurs des Maîtres des
Ténèbres. Ces créatures redoutables ont la faculté d'adopter l'apparence
des hommes, mais restent invulnérables aux armes ordinaires. L'être au
bâton noir éclate alors d'un rire terrifiant et une douleur fulgurante vous
déchire la tête. Il vient d'utiliser contre vous sa formidable Puissance
Psychique ; la situation est inquiétante : vous êtes en effet dominé par
un ennemi supérieur en nombre et il va falloir agir vite si vous voulez
survivre à cette attaque.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Souhaitez-vous abandonner votre cheval et plonger dans les broussailles pour vous y cacher ? Rendez-vous au :'))
    st.page_link("tomes/tome2/page_311.py", label="311", icon="📄")

    st.write_stream(stream_text('Si vous préférez prêter main forte aux hommes de Rhygar, rendez-vous au :'))
    st.page_link("tomes/tome2/page_59.py", label="59", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
