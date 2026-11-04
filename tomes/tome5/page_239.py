import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    has_kai,
    kai_rank,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=239, book=5)

fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
Si vous voulez pénétrer dans le Tombeau, vous devez
obligatoirement distraire la sentinelle ou bien la réduire au
silence.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez une Teinture de Ronces des cimetières, rendez-vous au :"))
    if has_item("POTION DE RONCES DES CIMETIÈRES"):
        st.page_link("tomes/tome5/page_260.py", label="260", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome5/page_260.py", label="260", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous ne possédez pas cet Objet Spécial, vous devrez arriver silencieusement à la hauteur du Garde, puis le neutraliser le plus rapidement et le plus silencieusement possible. A cette fin, utilisez la Table de Hasard pour obtenir un chiffre. Si vous maîtrisez les Disciplines Kaï de la Chasse, de l'Orientation et du Camouflage, ajoutez 2 points au chiffre que vous avez tiré. Si vous avez le titre de Gardien Kaï, ajoutez 3 points au chiffre obtenu."))
    if has_item("POTION DE RONCES DES CIMETIÈRES"):
        st.write("*Vous possédez la Teinture : la Table de Hasard ne vous concerne pas.*")
        st.page_link("tomes/tome5/page_324.py", label="324", icon="📄", disabled=True)
        st.page_link("tomes/tome5/page_303.py", label="303", icon="📄", disabled=True)
    else:
        roll = hazard_roll()
        if roll is not None:
            bonus = 0
            if has_kai("La Chasse") and has_kai("L'Orientation") and has_kai("Le Camouflage"):
                bonus += 2
            if kai_rank() >= 7:
                bonus += 3
            total = roll + bonus
            if bonus:
                st.write(f"*Bonus : +{bonus}, soit un total de {total}.*")
            if total <= 4:
                st.write_stream(stream_text("Si votre total est maintenant compris entre 0 et 4, rendez-vous au :"))
                st.page_link("tomes/tome5/page_324.py", label="324", icon="📄")
            else:
                st.write_stream(stream_text("S'il est de 5 ou plus, rendez-vous au :"))
                st.page_link("tomes/tome5/page_303.py", label="303", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
