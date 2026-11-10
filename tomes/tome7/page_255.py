import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=255, book=7)

fr_text = """
Dans sa chute, la tour a déraciné plusieurs arbres, et l'un d'entre
eux est resté en équilibre précaire sur le rempart de la forteresse.
Vous concentrez votre Maîtrise Kaï sur ce tronc et, après un
grand effort mental, vous parvenez à le faire basculer. L'arbre
tombe dans l'escalier et vous essayez de diriger sa chute pour
qu'il se mette en travers du vide, de chaque côté des marches.
Mais il prend beaucoup trop de vitesse et tombe sans que vous
puissiez le contrôler.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si votre total actuel d'ENDURANCE est supérieur ou égal à 20, ajoutez 2 au chiffre obtenu."))
    roll = hazard_roll(key="arbre")
    if roll is not None:
        total = roll + (2 if st.session_state.endurance >= 20 else 0)
        st.write(f"*Votre total est de {total}.*")
        # le livre écrit « 0, 1 ou 2 » puis « entre 5 et 8 » : 3 et 4 sont rattachés au 154 (0 à 4 dans l'original)
        if total <= 4:
            st.write_stream(stream_text("Si votre total est compris entre 0 et 4, rendez-vous au :"))
            st.page_link("tomes/tome7/page_154.py", label="154", icon="📄")
        elif total <= 8:
            st.write_stream(stream_text("Si votre total est compris entre 5 et 8, rendez-vous au :"))
            st.page_link("tomes/tome7/page_208.py", label="208", icon="📄")
        else:
            st.write_stream(stream_text("Si votre total est supérieur ou égal à 9, rendez-vous au :"))
            st.page_link("tomes/tome7/page_52.py", label="52", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
