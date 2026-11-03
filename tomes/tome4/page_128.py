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

check_inventory(current_page_number=128, book=4)

fr_text = """
Vous vous précipitez vers la trappe mais le Guerrier tente
d'empêcher votre fuite.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Utilisez la Table de Hasard pour obtenir un chiffre. Si vous maîtrisez la Discipline Kaï de la Chasse, vous ajouterez 3 au chiffre que vous aurez tiré.'))
    roll = hazard_roll()
    if roll is not None:
        total = roll + (3 if has_kai("La Chasse") else 0)
        if has_kai("La Chasse"):
            st.write(f"*Chasse : +3, soit un total de {total}.*")
        if total <= 4:
            st.write_stream(stream_text('Si le total obtenu est de 0 à 4, rendez-vous au :'))
            st.page_link("tomes/tome4/page_103.py", label="103", icon="📄")
        else:
            st.write_stream(stream_text('De 5 à 12, rendez-vous au :'))
            st.page_link("tomes/tome4/page_98.py", label="98", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
