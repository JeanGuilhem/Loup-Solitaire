import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    is_new_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=69, book=2)

fr_text = """
L'un des étrangers sort de sous sa cape un épieu noir qu'il tend devant
lui. D'un cône d'acier fixé à l'extrémité de l'épieu s'échappe soudain une
flamme bleuâtre et un éclair jaillit dans votre direction. Un fracas
assourdissant retentit lorsque l'éclair vient frapper le bouclier de
Rhygar. « Pas de quartiers ! » crie alors le Lieutenant Général en se
précipitant sur l'étranger à la lance de feu. L'épée de votre compagnon
transperce la cape de son adversaire mais ce dernier reste indemne.
Vous comprenez alors à qui vous avez affaire ; ces créatures vêtues de
capes sont en effet des Monstres d'Enfer, des êtres cruels au service des
Maîtres des Ténèbres dont ils sont les capitaines. Ils ont la faculté
d'adopter une apparence humaine, mais ils restent invulnérables aux
armes normales. Le Monstre d'Enfer que combat le Lieutenant Général
pousse un cri terrifiant qui vous déchire la tête ; aveuglé par cette
douleur fulgurante, vous trébuchez et vous tombez dans les broussailles
épaisses qui recouvrent le flanc boisé de la colline. Si vous ne maîtrisez
pas la Discipline Kaï du Bouclier Psychique, vous perdez 2 points
d'ENDURANCE sous la violence de l'attaque mentale du Monstre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if not has_kai("Le Bouclier Psychique"):
        if is_new_page():
            change_endurance(-2)
        st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_311.py", label="311", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
