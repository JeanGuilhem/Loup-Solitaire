import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=335, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Au moment précis où vous assénez le coup fatal, le Dhorgaan
disparaît sous vos yeux en un clin d'œil. Le Seigneur des
Ténèbres Haakon chancelle de stupeur en voyant s'anéantir sa
créature. La pierre étincelante lui échappe des mains, roule à
travers la pièce et s'arrête à mi-chemin entre vous deux.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous désirez tenter de vous emparer de la pierre, rendez-vous au :'))
    st.page_link("tomes/tome5/page_268.py", label="268", icon="📄")

    st.write_stream(stream_text('Si vous préférez ne pas vous soucier de cette pierre et attaquer Haakon sans perdre une seconde, rendez-vous au :'))
    st.page_link("tomes/tome5/page_390.py", label="390", icon="📄")

    st.write_stream(stream_text('Si vous maîtrisez la Discipline Kaï du Sixième Sens, rendez-vous au :'))
    if has_kai("Le Sixième Sens"):
        st.page_link("tomes/tome5/page_204.py", label="204", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_204.py", label="204", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
