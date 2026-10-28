import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=274, book=3)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Vous examinez attentivement l'autel et les deux piliers noirs qui
se dressent à sa surface. L'éclair qui avait jailli entre ces deux
piliers, les reliant par une mystérieuse énergie, s'est éteint au
moment précis où vous avez plongé le Glaive de Sommer dans le
cyclone démoniaque. Vous remarquez à présent que deux
boutons de pierre dépassent de la surface de l'autel, à l'endroit où
la statue était couchée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous maîtrisez la Discipline Kaï du Sixième Sens, rendez-vous au :'))
    if has_kai('Le Sixième Sens'):
        st.page_link("tomes/tome3/page_131.py", label="131", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome3/page_131.py", label="131", icon="📄", disabled=True)

    st.write_stream(stream_text('Si vous souhaitez appuyer sur ces boutons, rendez-vous au :'))
    st.page_link("tomes/tome3/page_227.py", label="227", icon="📄")

    st.write_stream(stream_text('Si vous préférez quitter le temple, rendez-vous au :'))
    st.page_link("tomes/tome3/page_306.py", label="306", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
