import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=381, book=5)

fr_text = """
En courant sous l'arche, vous heurtez de plein fouet un Garde du
Palais en habit noir. Vous avez les côtes enfoncées et la violence
du choc vous fait perdre l'équilibre, mais vous parvenez à vous
retenir au mur pour ne pas tomber. Le Garde, quant à lui, est
étendu sur le sol de tout son long. Mais, à une vitesse incroyable,
il sort une hache en acier brillant et vous attaque aux jambes.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous maîtrisez la Discipline Kaï de la Chasse, ajoutez 2 points au chiffre obtenu."))
    roll = hazard_roll()
    if roll is not None:
        bonus = 2 if has_kai("La Chasse") else 0
        total = roll + bonus
        if bonus:
            st.write(f"*Bonus de la Chasse : +2, soit un total de {total}.*")
        if total <= 4:
            st.write_stream(stream_text("Si votre total est compris entre 0 et 4, rendez-vous au :"))
            st.page_link("tomes/tome5/page_368.py", label="368", icon="📄")
        else:
            st.write_stream(stream_text("Si votre total est compris entre 5 et 11, rendez-vous au :"))
            st.page_link("tomes/tome5/page_252.py", label="252", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
