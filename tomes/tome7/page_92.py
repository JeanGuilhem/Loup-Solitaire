import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=92, book=7)

fr_text = """
Vous avancez d'un pas résolu dans le passage, sûr de votre force
et de votre adresse et prêt à affronter le garde qui aurait le
malheur de se trouver sur votre chemin. Vous distinguez par
endroits de sombres ouvertures sur les côtés et vous scrutez
attentivement le sol devant vous afin de dépister un éventuel
piège. Le tunnel devient de plus en plus sombre et humide. Vous
entendez au loin des claquements de fouet, des cris et des
gémissements pitoyables : de bien sinistres bruits qui évoquent
indéniablement la torture...
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez continuer à avancer, rendez-vous au :"))
    st.page_link("tomes/tome7/page_36.py", label="36", icon="📄")

    st.write_stream(stream_text("Si vous préférez rebrousser chemin pour emprunter plutôt l'autre passage, rendez-vous au :"))
    st.page_link("tomes/tome7/page_20.py", label="20", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
