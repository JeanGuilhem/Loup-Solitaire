import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=106, book=3)

fr_text = """
Lorsque vous franchissez l'ouverture pratiquée dans la porte,
vous voyez trois Barbares des Glaces qui avancent vers vous le
long du couloir. Ce sont des guerriers vêtus de fourrure et armés
d'épées en os qui sont chacune incrustée de dents pointues sur
toute la longueur de la lame. En dépit de la rapidité de leur
attaque, vous avez le temps de remarquer un étrange détail :
leurs yeux sont complètement blancs et dépourvus de pupilles.
Ils vous attaquent comme un seul homme, portant leurs coups et
évitant les vôtres d'un même mouvement. Il vous faut les
combattre comme s'il s'agissait d'un seul et même adversaire.
Ces trois Barbares sont insensibles à la Discipline Kaï de la
Puissance Psychique.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("BARBARES DES GLACES", 19, 36)], psychic_immune=True, flee_after=0)
    if outcome == "fled":
        st.write_stream(stream_text("Vous prenez la fuite en vous glissant à nouveau dans la salle que vous venez de quitter pour vous échapper ensuite par le passage orienté au nord. Rendez-vous au :"))
        st.page_link("tomes/tome3/page_145.py", label="145", icon="📄")
    elif outcome == "win":
        st.write_stream(stream_text("Si vous sortez vainqueur du combat, rendez-vous au :"))
        st.page_link("tomes/tome3/page_338.py", label="338", icon="📄")
    else:
        st.caption("Vous pouvez prendre la fuite à tout moment en vous glissant à nouveau dans la salle que vous venez de quitter pour vous échapper ensuite par le passage orienté au nord (145).")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
