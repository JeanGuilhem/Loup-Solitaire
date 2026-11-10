import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=227, book=7)

fr_text = """
Vous trouvez dans son sac et dans les poches de son armure en
cuir les objets suivants :

- 1 Corde
- 1 Couverture
- 1 Poignard
- 1 Fiole de Pilules Bleues
- 1 Bouteille d'Eau
- 1 Clé de Pouvoir

Tous ces objets, à l'exception de la Clé de Pouvoir qui est un
Objet Spécial, sont des objets de Sac à Dos. Choisissez parmi ces
objets ceux que vous souhaitez prendre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    for item, key in [
        ("CORDE", "corde"),
        ("COUVERTURE", "couverture"),
        ("POIGNARD", "poignard"),
        ("FIOLE DE PILULES BLEUES", "pilules"),
        ("BOUTEILLE D'EAU", "eau"),
        ("CLÉ DE POUVOIR", "cle"),
    ]:
        pickup_button(item, key=key)

    medic = has_magnakai("Science Médicale")
    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de la Science Médicale, vous pouvez identifier la nature des Pilules Bleues ; dans ce cas, rendez-vous au :"))
    st.page_link("tomes/tome7/page_43.py", label="43", icon="📄", disabled=not medic)
    st.write_stream(stream_text("Si vous ne maîtrisez pas cette discipline, continuez votre chemin en vous rendant au :"))
    st.page_link("tomes/tome7/page_323.py", label="323", icon="📄", disabled=medic)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
