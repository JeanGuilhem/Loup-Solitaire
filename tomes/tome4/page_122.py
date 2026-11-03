import streamlit as st
from combat import combat
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=122, book=4)

fr_text = """
Vous dégainez votre arme et la plainte du vent retentit aussitôt
avec plus de force, comme animée d'une brusque colère. Il
semble s'infiltrer en vous, faisant naître dans votre esprit de
terribles images d'horreur et de mort. Barraka vous voit hésiter
et vous porte un coup qui vous blesse à la joue. Vous perdez
aussitôt 1 point d'ENDURANCE. Cette soudaine douleur,
cependant, vous ramène à la réalité et le combat s'engage avec
votre cruel ennemi.
Il vous attaque en même temps à l'aide d'une redoutable
Puissance Psychique, qui réduira de 4 points votre total
d'HABILETÉ pendant toute la durée de l'affrontement, si vous ne
maîtrisez pas la Discipline Kaï du Bouclier Psychique. La force
exceptionnelle de sa volonté le rend en revanche invulnérable à
la Discipline Kaï de la Puissance Psychique.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-1)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-1)

    outcome = combat(
        [("BARRAKA", 25, 29)],
        hability_modifier=0 if has_kai("Bouclier psychique") else -4,
        psychic_immune=True,
    )
    if outcome == "win":
        st.write_stream(stream_text('Si vous remportez la victoire, rendez-vous au :'))
        st.page_link("tomes/tome4/page_350.py", label="350", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
