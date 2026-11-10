import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=313, book=7)

fr_text = """
Le manque d'oxygène vous donne des vertiges (vous perdez 3
points d'ENDURANCE) mais vous essayez d'oublier la douleur et
vous continuez à avancer.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-3)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-3)

    # le texte français a perdu une phrase : dans l'original, on ajoute le chiffre tiré à son total d'ENDURANCE
    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre et ajoutez-le à votre total d'ENDURANCE."))
    roll = hazard_roll(key="oxygene")
    if roll is not None:
        total = roll + st.session_state.endurance
        st.write(f"*{roll} + {st.session_state.endurance} (ENDURANCE) = **{total}**.*")
        st.write_stream(stream_text("Si votre total est supérieur ou égal à 10, rendez-vous au :"))
        st.page_link("tomes/tome7/page_4.py", label="4", icon="📄", disabled=total < 10)
        st.write_stream(stream_text("S'il est inférieur ou égal à 9, rendez-vous au :"))
        st.page_link("tomes/tome7/page_263.py", label="263", icon="📄", disabled=total >= 10)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
