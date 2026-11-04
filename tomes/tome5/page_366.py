import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, ls_death

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=366, book=5)

fr_text = """
Vous attendez nerveusement que la chance vous sourie avant
d'aller ouvrir la porte, mais malheureusement, la pluie de flèches
qui rebondissent sur le mur et le parapet est de plus en plus
dense. Tout à coup, des bruits de pas vous glacent le sang : les
Drakkars sont en train de dévaler l'escalier. C'est maintenant ou
jamais ! Vous vous relevez rapidement et vous courez vers la
porte. Vous tirez le verrou avec des mains tremblantes mais, au
moment où la porte va s'ouvrir, vous ressentez une douleur
fulgurante dans le dos : vous êtes touché ! Une seconde flèche
vient s'enfoncer profondément dans votre épaule et vous vous
écrasez violemment contre la porte. Un voile noir tombe devant
vos yeux, et vous ne voyez même pas les Drakkars qui se
précipitent vers vous en brandissant leurs noires épées pour vous
donner le coup de grâce. Les lames vous transpercent de part en
part mais vous ne sentez rien. Vous êtes déjà mort. Votre vie
ainsi que les espoirs du Sommerlund se terminent ici.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    show_illustrations()
    ls_death()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
