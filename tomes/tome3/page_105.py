import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=105, book=3)

fr_text = """
Vous faites une chute d'une cinquantaine de mètres et vous
tombez sur un énorme tas de neige poudreuse. Vous êtes secoué
et vous avez le souffle coupé, mais vous n'êtes pas blessé. Il vous
faut presque une demi-heure pour vous dégager de cette masse
de neige et quand enfin vous en émergez, le spectacle qui s'offre à
vos yeux vous laisse bouche bée. Une immense caverne s'étend
devant vous ; de gigantesques stalactites de cristal pendent d'une
voûte de glace et la neige fondante qui s'en égoutte peu à peu
emplit l'espace d'une étrange musique. Vous êtes en train de
contempler un monde inconnu que peu de Sommerlundois ont
eu l'occasion de voir : vous venez en effet de tomber dans les
Grottes de Kalte. Cette caverne est une toute petite partie d'un
immense labyrinthe souterrain bâti par les Anciens des siècles
plus tôt, à une époque où les Sommerlundois, pas plus que les
Maîtres des Ténèbres, n'avaient encore mis le pied sur les terres
de Magnamund. Ses vastes tunnels, ses temples et ses salles ont
abrité jadis une race de créatures pour qui la glace était un
environnement naturel ; sous ces voûtes résonnaient leurs pas et
l'écho de leurs paroles. Des coupes de M'iare pendent encore au
plafond, baignant la caverne d'une lumière éternelle. Vous
appelez à grands cris, la tête levée vers la cheminée par laquelle
vous êtes tombé, mais personne ne vous répond. Irian et Fenor
sont persuadés que vous n'avez pas survécu et ils ont déjà
entrepris de rejoindre le vaisseau Cardonal. Les parois de la
caverne sont raides et lisses : il vous serait impossible de les
escalader pour remonter à la surface. Au loin, en direction du
nord, vous apercevez un tunnel grossièrement creusé dans la
pierre. Il existe un tunnel semblable à l'ouest.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez explorer le tunnel situé au nord, rendez-vous au :"))
    st.page_link("tomes/tome3/page_321.py", label="321", icon="📄")
    st.write_stream(stream_text("Si vous préférez explorer le tunnel qui se trouve à l'ouest, rendez-vous au :"))
    st.page_link("tomes/tome3/page_275.py", label="275", icon="📄")
    st.write_stream(stream_text("Enfin, si vous maîtrisez la Discipline Kaï du Sixième Sens, rendez-vous au :"))
    if has_kai("Le Sixième Sens"):
        st.page_link("tomes/tome3/page_64.py", label="64", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome3/page_64.py", label="64", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
