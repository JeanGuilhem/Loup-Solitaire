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

check_inventory(current_page_number=198, book=5)

fr_text = """
Tandis que le corps inerte de l'Officier heurte violemment la
porte défoncée de la cave, les Sharnazims reculent et laissent
passer Maouk qui apparaît dans l'encadrement de la porte en
brandissant une fléchette. « Je vous tiens maintenant ! », dit-il
d'une voix sifflante en lançant la flèche vers votre poitrine.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous maîtrisez la Discipline Kaï de la Chasse, ajoutez 3 au chiffre obtenu."))
    roll = hazard_roll()
    if roll is not None:
        bonus = 3 if has_kai("La Chasse") else 0
        total = roll + bonus
        if bonus:
            st.write(f"*Bonus : +{bonus}, soit un total de {total}.*")
        if total <= 6:
            st.write_stream(stream_text("Si le résultat obtenu est compris entre 0 et 6, rendez-vous au :"))
            st.page_link("tomes/tome5/page_25.py", label="25", icon="📄")
        else:
            st.write_stream(stream_text("Si le résultat obtenu est compris entre 7 et 9, rendez-vous au :"))
            st.page_link("tomes/tome5/page_141.py", label="141", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
