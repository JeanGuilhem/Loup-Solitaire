import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_flag,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=27, book=3)

fr_text = """
Vous avancez avec difficulté le long des sinistres montagnes
pendant presque une heure, sans trouver d'abri pour échapper
au vent glacé. A moins que vous ne vous soyez enduit le torse
d'huile de Bakanal, vous perdrez 2 points d'ENDURANCE en
raison du froid extrême.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if has_flag("huile de Bakanal"):
        st.success("*L'huile de Bakanal dont vous êtes enduit vous protège du froid.*")
    else:
        if is_new_page():
            change_endurance(-2)
        st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)

    st.write_stream(
        stream_text("Si vous souhaitez poursuivre votre chemin pour essayer de trouver un abri, rendez-vous au :")
    )
    st.page_link("tomes/tome3/page_314.py", label="314", icon="📄")

    st.write_stream(
        stream_text(
            "Si vous préférez creuser à la main un trou dans la neige pour y passer la nuit, rendez-vous au :"
        )
    )
    st.page_link("tomes/tome3/page_205.py", label="205", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
