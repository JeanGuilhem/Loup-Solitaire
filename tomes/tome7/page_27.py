import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    show_illustrations,
    show_map,
)
from text import fr_unknown_magnakai
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=27, book=7)

fr_text = """
Vous progressez prudemment à travers les décombres moussus,
puis vous faites halte le temps de reprendre votre souffle et
d'observer l'édifice en ruine. La vision est désolante : il ne reste
plus qu'une carcasse de pierres piquées d'humidité, envahie par
les plantes grimpantes. Un grand incendie a dû ravager
l'intérieur de la forteresse, ce qui expliquerait un tel
délabrement. Au centre de la forteresse s'étend la Grande
Galerie... ou ce qu'il en reste. C'est une salle de dimensions
imposantes, dont l'aspect sinistre est renforcé par de fréquents
éclairs de lumière verte. Le parquet à demi calciné est couvert de
moisissures, et des arbres tordus ont poussé le long des murs en
étirant leur branchage à travers les fissures de la pierre. Juste au
moment où vous vous apprêtez à pénétrer dans la salle, vous
entendez quelque chose siffler au-dessus de votre tête et vous
vous arrêtez net : une sombre silhouette aux yeux rouges est en
train de prendre forme dans l'encadrement de la porte ! Un
frisson vous parcourt l'échine lorsque vous la sentez passer près
de vous en produisant un déplacement d'air glacial. Vous faites
volte-face et vous découvrez alors que la créature plane
maintenant au-dessus de vous en brandissant au bout d'une
chaîne une grosse boule de métal hérissée de pointes. Votre
agresseur pousse un cri inhumain, puis fait tournoyer son fléau
d'armes vers votre visage.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de l'Écran Psychique, rendez-vous au :"))
    if has_magnakai("Écran Psychique"):
        st.page_link("tomes/tome7/page_38.py", label="38", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome7/page_38.py", label="38", icon="📄", disabled=True)

    if not has_magnakai("Écran Psychique"):
        st.write_stream(stream_text("Si vous ne maîtrisez pas cette discipline, préparez-vous à combattre car vous n'avez plus le temps de vous enfuir. En raison de la rapidité de l'attaque de votre adversaire, déduisez 3 points de votre total d'HABILETÉ durant les trois premiers Assauts, sauf si vous maîtrisez la Discipline Magnakaï de l'Art de la Chasse."))
        outcome = combat(
            [("OUDAKON", 20, 29)],
            first_round_modifier=0 if has_magnakai("Art de la Chasse") else -3,
            first_rounds=3,
        )
        if outcome == "win":
            st.write_stream(stream_text('Si vous sortez vainqueur du combat, rendez-vous au :'))
            st.page_link("tomes/tome7/page_5.py", label="5", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
