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

check_inventory(current_page_number=118, book=7)

fr_text = """
Vous sentez une vague d'énergie submerger votre corps tout
entier lorsque vos doigts s'approchent de la Pierre de la Sagesse
de Herdos (votre total d'ENDURANCE retrouve son niveau
initial). Un fourmillement vous parcourt de la tête aux pieds, et
toute la fatigue causée par les récentes épreuves que vous avez
subies se trouve balayée d'un coup par un regain de force. Vous
voici frais et dispos, prêt à affronter la situation. Vous entrez
dans le rayon bleu et vous vous sentez immédiatement soulevé et
emporté sur les traces de l'infâme Zahda qui s'efforce à présent
de rester au centre de la colonne de lumière. Vous sentez qu'il a
terriblement peur de vous. En voyant que vous gagnez du terrain
sur lui, il tire un poignard étincelant et fait volte-face pour vous
affronter. Une fois que vous êtes à sa portée, il passe
brusquement à l'attaque. Le Seigneur Zahda est insensible à la
Puissance Psychique, mais il est vulnérable au Foudroiement
Psychique. Par ailleurs, si vous maîtrisez la Discipline Magnakaï
de l'Art de la Chasse, ajoutez 2 points à votre total d'HABILETÉ
pour toute la durée du combat.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # la Pierre de la Sagesse rend tout le total d'ENDURANCE
    if is_new_page():
        st.session_state.zahda_heal = st.session_state.total_endurance - st.session_state.endurance
        change_endurance(st.session_state.zahda_heal)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=st.session_state.get("zahda_heal", 0))

    outcome = combat([("SEIGNEUR ZAHDA", 23, 45)], psychic_power_immune=True,
                     hability_modifier=2 if has_magnakai("Art de la Chasse") else 0)
    if outcome == "win":
        st.write_stream(stream_text("Si vous sortez vainqueur de cet affrontement, rendez-vous au :"))
        st.page_link("tomes/tome7/page_200.py", label="200", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
