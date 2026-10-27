import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=169, book=2)

fr_text = """
Découragé, vous quittez la maison de jeu et vous retournez au relais de
diligence ; au loin, vous apercevez la porte Est de la ville. La diligence
de Durenor attend juste à côté. Or, il vous faut à tout prix gagner Port
Bax, l'avenir du Sommerlund en dépend. Vous vous arrangez donc pour
passer derrière le garde qui surveille la diligence et vous montez dans le
véhicule sans qu'il vous ait vu. A mesure que l'heure du départ
approche, cinq autres passagers montent à leur tour et s'assoient autour
de vous. Le garde claque alors la portière et le voyage pour Port Bax
commence.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            "Utilisez la Table de Hasard pour obtenir un chiffre. Entre 0 et 3, rendez-vous au 39. "
            "Entre 4 et 6, rendez-vous au 249. Entre 7 et 9, rendez-vous au 339."
        )
    )
    number = hazard_roll()
    if number is not None and 0 <= number <= 3:
        st.page_link("tomes/tome2/page_39.py", label="39", icon="📄")
    elif number is not None and 4 <= number <= 6:
        st.page_link("tomes/tome2/page_249.py", label="249", icon="📄")
    elif number is not None and 7 <= number <= 9:
        st.page_link("tomes/tome2/page_339.py", label="339", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
