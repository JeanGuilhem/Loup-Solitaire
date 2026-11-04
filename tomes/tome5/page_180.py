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

check_inventory(current_page_number=180, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Alors que le deuxième Garde s'effondre à vos pieds, vous
remarquez que le premier Garde s'est remis de votre coup. Il
extrait un poignard de sa botte et, levant le bras, il s'apprête à
vous le lancer.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï de la Puissance Psychique, rendez-vous au :"))
    if has_kai("Puissance psychique"):
        st.page_link("tomes/tome5/page_45.py", label="45", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_45.py", label="45", icon="📄", disabled=True)

        st.write_stream(stream_text("Si vous ne maîtrisez pas cette Discipline, utilisez la Table de Hasard pour obtenir un chiffre. Si vous possédez la Discipline Kaï du Sixième Sens, ou celle de la Chasse, ajoutez 3 au chiffre obtenu."))
        roll = hazard_roll()
        if roll is not None:
            bonus = 3 if has_kai("Le Sixième Sens") or has_kai("La Chasse") else 0
            total = roll + bonus
            if bonus:
                st.write(f"*Bonus : +{bonus}, soit un total de {total}.*")
            if total <= 5:
                st.write_stream(stream_text("Si le résultat obtenu est compris entre 0 et 5, rendez-vous au :"))
                st.page_link("tomes/tome5/page_120.py", label="120", icon="📄")
            else:
                st.write_stream(stream_text("S'il est compris entre 6 et 12, rendez-vous au :"))
                st.page_link("tomes/tome5/page_193.py", label="193", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
