import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_flag,
    has_kai,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=23, book=5)

fr_text = """
L'ascension serait facile s'il n'y avait point cette vapeur brûlante
qui vous pique le visage et les mains, faisant boursoufler
douloureusement votre peau. Vous perdez 1 point d'ENDURANCE.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-1)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-1)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous avez perdu l'usage d'un bras, déduisez 3 points du chiffre obtenu. Si vous maîtrisez la Discipline Kaï de la Chasse, ajoutez 2 points à ce chiffre."))
    roll = hazard_roll()
    if roll is not None:
        bonus = 0
        if has_flag("bras paralysé"):
            bonus -= 3
        if has_kai("La Chasse"):
            bonus += 2
        total = roll + bonus
        if bonus:
            st.write(f"*Modificateur : {bonus:+d}, soit un total de {total}.*")
        if total <= -1:
            st.write_stream(stream_text('Si le résultat est compris entre -3 et -1, rendez-vous au :'))
            st.page_link("tomes/tome5/page_77.py", label="77", icon="📄")
        elif total <= 6:
            st.write_stream(stream_text('Si le résultat est compris entre 0 et 6, rendez-vous au :'))
            st.page_link("tomes/tome5/page_192.py", label="192", icon="📄")
        else:
            st.write_stream(stream_text('Enfin, si le résultat est compris entre 7 et 11, rendez-vous au :'))
            st.page_link("tomes/tome5/page_114.py", label="114", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
