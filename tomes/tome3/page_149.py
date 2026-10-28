import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=149, book=3)

fr_text = """
Vous faites habilement un pas de côté pour essayer d'éviter le
coup que le Barbare des Glaces vous porte avec sa lance à la
pointe d'os.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre qui vous indiquera si vous avez réussi à esquiver. Si vous maîtrisez la Discipline Kaï de l'Orientation, celle de la Chasse ou celle du Sixième Sens, vous aurez le droit d'ajouter 2 au chiffre donné par la Table."))
    bonus = 2 if (has_kai("L'Orientation") or has_kai("La Chasse") or has_kai("Le Sixième Sens")) else 0
    number = hazard_roll()
    if number is not None:
        total = number + bonus
        if bonus:
            st.write(f"*Grâce à votre Discipline Kaï, vous ajoutez 2 : total {total}.*")
        if total <= 4:
            st.write_stream(stream_text("Rendez-vous au :"))
            st.page_link("tomes/tome3/page_286.py", label="286", icon="📄")
        else:
            st.write_stream(stream_text("Rendez-vous au :"))
            st.page_link("tomes/tome3/page_333.py", label="333", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
