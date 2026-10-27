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

check_inventory(current_page_number=193, book=2)

fr_text = """
Le voyage de retour au royaume du Sommerlund se déroule sous de
mauvais auspices. De gros nuages noirs s'amoncellent à l'horizon et un
vent violent agite la mer sans relâche. A la nuit tombée, de grands
éclairs aveuglants déchirent l'obscurité, suivis par des roulements de
tonnerre si fracassants que le navire amiral en est tout ébranlé depuis
l'extrémité de sa quille jusqu'à la pointe de ses mâts. La plupart des
soldats qui voyagent à bord de la flotte sont des montagnards qui n'ont
aucune expérience de la mer et au bout du troisième jour, une bonne
moitié d'entre eux sont cloués au lit, incapables de se lever. Lord Axim
semble au bord du désespoir. « Puisse cette tempête se calmer, dit-il,
car même si la flotte arrivait intacte au bout du voyage, nos hommes
seraient trop faibles pour pouvoir combattre, après avoir subi une telle
épreuve. » Et le lendemain, comme si sa prière avait été entendue,
l'aube se lève dans un ciel apaisé qui annonce la fin de la tourmente.
Mais les eaux calmes à présent où navigue la flotte cachent un péril
plus redoutable encore que la tempête des jours passés.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_100.py", label="100", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
