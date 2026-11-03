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

check_inventory(current_page_number=271, book=4)

fr_text = """
Vous êtes parvenu au milieu du pont lorsque l'un des Gardes tire
sur la corde suspendue au plafond. En jetant un coup d'œil par-
dessus votre épaule, vous constatez avec horreur que la corde
passe dans une série d'anneaux de métal pour aboutir à deux
broches de fixation qui maintiennent la passerelle accrochée au
bord du puits. Lorsque la corde se tend, les broches de fixation se
détachent.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Utilisez la Table de Hasard pour obtenir un chiffre. Si vous maîtrisez la Discipline Kaï de la Chasse, vous ajouterez 2 au chiffre que vous aurez tiré.'))
    roll = hazard_roll()
    if roll is not None:
        total = roll + (2 if has_kai("La Chasse") else 0)
        if has_kai("La Chasse"):
            st.write(f"*Chasse : +2, soit un total de {total}.*")
        if total <= 6:
            st.write_stream(stream_text('Si vous obtenez un total de 0 à 6, rendez-vous au :'))
            st.page_link("tomes/tome4/page_9.py", label="9", icon="📄")
        else:
            st.write_stream(stream_text('De 7 à 11, rendez-vous au :'))
            st.page_link("tomes/tome4/page_104.py", label="104", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
