import streamlit as st
from combat import combat
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

check_inventory(current_page_number=237, book=2)

fr_text = """
Les Zombies morts sont étendus à vos pieds. A présent, la peur que les
soldats éprouvaient devant les morts vivants a fait place à la haine. Un
chœur de cris de guerre retentit sur le pont et vous montez à l'abordage
du vaisseau fantôme, suivis par les centaines de soldats ivres de rage.
Les Zombies sont fauchés sous l'assaut comme des épis de blé par une
faux. Puis soudain, une silhouette drapée dans une longue cape vous
interdit le passage, brandissant dans sa main squelettique une épée à la
lame recourbée. C'est un MONSTRE D'ENFER et il vous faut le
combattre jusqu'à la mort de l'un d'entre vous.
C'est un mort vivant et vous avez donc le droit, en vertu de la puissance
du Glaive de Sommer, de multiplier par 2 tous les points
d'ENDURANCE qu'il perdra au combat. Mais rappelez-vous qu'il est
insensible à la Discipline Kaï de la Puissance Psychique.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("MONSTRE D'ENFER", 23, 30)], psychic_immune=True, undead=True)
    if outcome == "win":
        st.write_stream(stream_text('Si vous êtes vainqueur, rendez-vous au :'))
        st.page_link("tomes/tome2/page_309.py", label="309", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
