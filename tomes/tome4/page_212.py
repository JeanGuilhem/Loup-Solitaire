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

check_inventory(current_page_number=212, book=4)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Une odeur d'humidité et de pourriture baigne le puits de mine.
Vous ordonnez à l'un de vos hommes de monter à l'échelle pour
vérifier qu'elle est toujours solide. Le patrouilleur atteint bientôt
le niveau supérieur et vous fait signe de le suivre. Vous vous
retrouvez alors dans un tunnel qui mène à une petite salle de
forme ovale creusée grossièrement dans la roche. Un étrange
liquide gluant brille sur le sol.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous maîtrisez la Discipline Kaï de la Communication Animale, rendez-vous au :'))
    if has_kai("Communication Animale"):
        st.page_link("tomes/tome4/page_41.py", label="41", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome4/page_41.py", label="41", icon="📄", disabled=True)

    st.write_stream(stream_text('Sinon, vous devrez chercher une issue à cette salle en vous rendant au :'))
    st.page_link("tomes/tome4/page_276.py", label="276", icon="📄", disabled=has_kai("Communication Animale"))

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
