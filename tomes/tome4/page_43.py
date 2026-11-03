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

check_inventory(current_page_number=43, book=4)

fr_text = """
Si vous voulez survivre à cette attaque, vous devrez faire preuve
de rapidité et de précision. Vous brandissez votre arme, prêt à
frapper.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous possédez la Discipline Kaï de la Maîtrise Psychique de la Matière ou celle de la Maîtrise des Armes, vous ajouterez 1 au chiffre tiré. Si vous maîtrisez la Discipline Kaï de la Chasse ou du Sixième Sens, vous ajouterez 2 au chiffre donné par la Table."))
    roll = hazard_roll()
    if roll is not None:
        bonus = 0
        if has_kai("Maîtrise Psychique de la Matière") or has_kai("La Maîtrise des Armes"):
            bonus += 1
        if has_kai("La Chasse") or has_kai("Le Sixième Sens"):
            bonus += 2
        total = roll + bonus
        if bonus:
            st.write(f"*Bonus : +{bonus}, soit un total de {total}.*")
        if total <= 6:
            st.write_stream(stream_text("Si vous obtenez un total de 0 à 6, rendez-vous au :"))
            st.page_link("tomes/tome4/page_262.py", label="262", icon="📄")

        else:
            st.write_stream(stream_text("Si ce total est de 7 ou plus, rendez-vous au :"))
            st.page_link("tomes/tome4/page_111.py", label="111", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
