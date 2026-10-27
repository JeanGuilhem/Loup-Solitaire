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

check_inventory(current_page_number=175, book=2)

fr_text = """
« Il semble que l'oiseau se soit envolé », dit le capitaine. Il vous montre
alors un canot qui file à bonne allure en direction d'un autre navire. «
Regardez bien ce vaisseau, il n'a pas de pavillon et sa forme me paraît
bien étrange. Je n'en ai encore jamais vu de semblable. » Vous observez
le canot qui rejoint en quelques instants le mystérieux navire. Et
soudain, comme par magie, un brouillard venu d'on ne sait où se lève
sur la mer et enveloppe le vaisseau. Moins d'une minute plus tard, le
navire et le brouillard ont tous deux disparu.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            "Utilisez la Table de Hasard pour obtenir un chiffre. Entre 0 et 4, rendez-vous au 53. "
            "Entre 5 et 9, rendez-vous au 209."
        )
    )
    number = hazard_roll()
    if number is not None and 0 <= number <= 4:
        st.page_link("tomes/tome2/page_53.py", label="53", icon="📄")
    elif number is not None and 5 <= number <= 9:
        st.page_link("tomes/tome2/page_209.py", label="209", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
