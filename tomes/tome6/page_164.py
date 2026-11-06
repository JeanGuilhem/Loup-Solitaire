import streamlit as st
from combat import combat
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=164, book=6)

fr_text = """
Votre remarquable Instinct d'Intuition vous permet de déceler
qu'un projectile meurtrier file à la vitesse de l'éclair en direction
de votre torse. Soudain, tout semble se passer au ralenti : vous
faites un bond de côté, et la flèche ne fait que vous érafler la peau
(vous perdez cependant 2 points d'ENDURANCE). L'instant
d'après, vous voyez votre agresseur jeter furieusement son
arbalète à terre. A travers la visière de son heaume, une voix
étouffée vous parvient : « A mort, homme du Nord ! » Sur ces
mots, le guerrier surgit hors de la Porte de Denka et vous charge
au grand galop en brandissant une hache, vous ne pouvez pas
l'éviter et vous devez vous battre jusqu'à ce que mort s'ensuive.
"""

fr_text_2 = """
En raison de la rapidité fulgurante de cette attaque, vous ne
pouvez pas vous servir de votre Arc. En revanche, si vous
maîtrisez la Discipline Magnakaï du Contrôle Animal, vous
pouvez ajouter 1 point à votre total d'HABILETÉ pour toute la
durée du combat.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write(fr_text_2)

    if is_new_page():
        change_endurance(-2)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)

    outcome = combat([("ASSASSIN À L'ARMURE", 24, 26)], hability_modifier=1 if has_magnakai("Contrôle Animal") else 0)
    if outcome == "win":
        st.write_stream(stream_text("Si vous en sortez vainqueur, rendez-vous au :"))
        st.page_link("tomes/tome6/page_28.py", label="28", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
