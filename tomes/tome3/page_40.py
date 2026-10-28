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

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=40, book=3)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Vous avez fait une chute de plus de 15 mètres, mais vous avez
atterri sans dommage sur un tas de neige. Essuyant vos yeux
couverts de neige glacée, vous restez bouche bée devant le
spectacle qui s'offre à vous. Une vaste caverne s'étend aussi loin
que porte votre regard ; d'immenses stalactites de cristal pendent
d'un plafond de glace et la neige fondue qui s'égoutte sans cesse
emplit les lieux d'une étrange musique. Vous êtes en train de
contempler un monde inconnu que fort peu de Sommerlundois
ont jamais vu : ce sont en effet les Grottes de Kalte qui s'ouvrent
ainsi devant vous. Cet immense labyrinthe souterrain a été bâti
par les Anciens, bien avant que les Sommerlundois, ou même les
Maîtres des Ténèbres, ne viennent s'installer sur les terres de
Magnamund. Ses larges galeries, ses temples et ses vastes salles
ont abrité jadis une race de créatures pour qui la glace était un
environnement naturel, des créatures dont les pas et les voix ont
empli de leur écho ces espaces polaires. Des coupes de M'iare
sont toujours suspendues au plafond, répandant une lumière
inquiétante et éternelle. Vous suivez un large canal de neige
fondue qui, au bout de 3 kilomètres, disparaît sous un mur de
glace miroitante. Un pont de glace mène alors à un tunnel qui
aboutit bientôt à une bifurcation.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez prendre l'embranchement de gauche, rendez-vous au :"))
    st.page_link("tomes/tome3/page_125.py", label="125", icon="📄")

    st.write_stream(stream_text('Si vous préférez emprunter celui de droite, rendez-vous au :'))
    st.page_link("tomes/tome3/page_184.py", label="184", icon="📄")

    st.write_stream(stream_text("Enfin, si vous maîtrisez la Discipline Kaï de l'Orientation, rendez-vous au :"))
    if has_kai("L'Orientation"):
        st.page_link("tomes/tome3/page_255.py", label="255", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome3/page_255.py", label="255", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
