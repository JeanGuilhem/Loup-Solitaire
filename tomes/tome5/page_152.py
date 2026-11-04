import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
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

check_inventory(current_page_number=152, book=5)

fr_text = """
Vous vous collez aux pierres du mur en essayant d'éviter de
regarder les cours et les jardins du Palais à plusieurs dizaines de
mètres en contrebas. Vous vous mordez nerveusement les lèvres
en attendant que les Gardes s'éloignent, mais ils n'en font rien.
La nuit va bientôt tomber et ils viennent fermer les grilles des
fenêtres du Palais. Vous pouvez entendre le cliquetis des clés
dans les serrures et les grilles grincer sur leurs gonds. Tous ces
bruits vous font frémir et vous comprenez que vous êtes enfermé,
à l'extérieur ! A votre gauche, la corniche fait le tour d'un dôme.
Sous ce dôme se trouve la cantine. Si seulement vous pouviez
parvenir à longer la corniche centimètre par centimètre, vous
pourriez peut-être trouver une fenêtre ouverte de l'autre côté.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous maîtrisez la Discipline Kaï de la Chasse, ajoutez 2 au chiffre obtenu. Si vous avez le titre de Savant Kaï, ajoutez 2 autres points."))
    roll = hazard_roll()
    if roll is not None:
        bonus = 0
        if has_kai("La Chasse"):
            bonus += 2
        if kai_rank() >= 9:
            bonus += 2
        total = roll + bonus
        if bonus:
            st.write(f"*Bonus : +{bonus}, soit un total de {total}.*")
        if total <= 2:
            st.write_stream(stream_text("Si votre total est compris entre 0 et 2, rendez-vous au :"))
            st.page_link("tomes/tome5/page_5.py", label="5", icon="📄")
        elif total <= 8:
            st.write_stream(stream_text("Si votre total est compris entre 3 et 8, rendez-vous au :"))
            st.page_link("tomes/tome5/page_38.py", label="38", icon="📄")
        else:
            st.write_stream(stream_text("Si votre total est compris entre 9 et 13, rendez-vous au :"))
            st.page_link("tomes/tome5/page_87.py", label="87", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
