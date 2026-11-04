import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=57, book=5)

fr_text = """
La porte n'est pas fermée à clé et vous avez soudain l'intuition
qu'un danger imminent vous menace. En effet, si cette pièce se trouve être l'Herboristerie Impériale où l'on garde
précieusement, tel un trésor, l'herbe d'Oede, alors pourquoi la
porte n'en est-elle pas verrouillée et sévèrement gardée ? Frémissant d'anxiété, vous vous glissez prudemment à
l'intérieur. Il s'agit effectivement de l'Herboristerie, et vous
regardez avec fascination les différents liquides colorés qui
bouillonnent à travers l'enchevêtrement des tubes de cornues en
verre et qui soufflent, de temps à autre, des jets de vapeurs
bleuâtres. Des centaines de jarres renfermant toutes sortes
d'herbes et d'épices sont alignées le long des murs et dix grands
plateaux en cuivre, contenant une poudre aux couleurs irisées,
pendent du plafond noirci par la suie. Vous commencez à
inspecter le contenu des jarres et vous découvrez soudain la
raison pour laquelle la porte n'était pas fermée à clé : le gardien
des lieux - une créature féline aux yeux cruels - s'avance en
rampant lentement vers vous et pousse un grognement féroce
avant de passer à l'attaque.
Si vous avez déjà eu l'occasion de vous battre contre un Elix,
ajoutez 2 points à votre total d'ENDURANCE pour toute la durée
de ce combat. Vous ne pouvez pas fuir et vous devrez mener le
combat jusqu'à ce que mort s'ensuive.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # le texte dit « ENDURANCE », lu comme un bonus d'HABILETÉ pour le combat
    elix_before = st.checkbox("Vous avez déjà combattu un Elix (au tome 4, par exemple)", key="elix_before")
    outcome = combat([("ELIX", 17, 32)], hability_modifier=2 if elix_before else 0)
    if outcome == "win":
        st.write_stream(stream_text("Si vous sortez vainqueur de cet affrontement, rendez-vous au :"))
        st.page_link("tomes/tome5/page_2.py", label="2", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
