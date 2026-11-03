import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=304, book=4)

fr_text = """
Un seul coup de votre arme suffit à sectionner le tentacule qui
emprisonne le pied du patrouilleur. L'homme vous remercie avec
chaleur, puis tranche à son tour l'extrémité d'un autre tentacule
gluant qui émerge de l'eau boueuse. Soudain, un craquement
terrifiant retentit. Un troisième tentacule vient de fracasser le
fond du bateau en projetant l'embarcation dans les airs. Vous
êtes alors précipité dans l'eau glacée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre."))
    roll = hazard_roll()
    if roll is not None:
        if roll <= 4:
            st.write_stream(stream_text("Si vous tirez un chiffre de 0 à 4, rendez-vous au :"))
            st.page_link("tomes/tome4/page_47.py", label="47", icon="📄")
        else:
            st.write_stream(stream_text("Si vous tirez un chiffre de 5 à 9, rendez-vous au :"))
            st.page_link("tomes/tome4/page_234.py", label="234", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
