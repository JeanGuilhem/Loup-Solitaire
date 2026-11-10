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

check_inventory(current_page_number=269, book=7)

fr_text = """
Vous passez à travers le faisceau de lumière rouge mais, aussitôt
après, vous sentez des picotements dans tout le corps, et vos
muscles se raidissent douloureusement. Vos membres sont
anormalement lourds, et vous éprouvez bientôt la plus grande
difficulté à mettre un pied devant l'autre. Soudain, le sol se met à
trembler ; une grosse dalle en pierre s'élève et vient obstruer
l'entrée. Vous entendez un sifflement bruyant, et une étrange
odeur emplit vos narines. Le temps que vous réalisiez qu'un
puissant gaz soporifique s'échappe d'orifices cachés dans le
plafond, vous succombez déjà à son irrésistible pouvoir.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_165.py", label="165", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
