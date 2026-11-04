import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    kai_rank,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=392, book=5)

fr_text = """
La bière épaisse et crémeuse a un goût de pomme verte. Vous
videz la moitié de la chope et vous essuyez la mousse restée sur
vos lèvres du revers de votre manche.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si votre total d'ENDURANCE est inférieur à 15, ôtez 2 points au chiffre que vous avez tiré. Si votre total d'ENDURANCE est supérieur à 25, ajoutez 2 points au chiffre que vous avez tiré. Si vous possédez le titre de Savant Kaï, ajoutez 3 à ce chiffre."))
    roll = hazard_roll()
    if roll is not None:
        bonus = 0
        if st.session_state.endurance < 15:
            bonus -= 2
        elif st.session_state.endurance > 25:
            bonus += 2
        if kai_rank() >= 9:
            bonus += 3
        total = roll + bonus
        if bonus:
            st.write(f"*Modificateur : {bonus:+d}, soit un résultat de {total}.*")
        if total < 7:
            st.write_stream(stream_text("Si le résultat obtenu est inférieur à 7, rendez-vous au :"))
            st.page_link("tomes/tome5/page_364.py", label="364", icon="📄")
        else:
            st.write_stream(stream_text("Si ce résultat est de 7 ou plus, rendez-vous au :"))
            st.page_link("tomes/tome5/page_218.py", label="218", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
