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

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=335, book=4)

fr_text = """
Le tunnel aboutit bientôt à une vaste salle séparée en deux par
un profond puits de mine. Une passerelle permet de le franchir,
mais elle est gardée par un soldat vêtu d'une armure de cuir
quelque peu fatiguée. Il est en train de tailler un bloc de bois et
grommelle en se plaignant d'avoir sans cesse à accomplir de
basses besognes. De l'autre côté de la salle, un tunnel s'ouvre
dans le mur ouest. Pour l'atteindre il vous faudra franchir le
pont.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if has_kai("Le Camouflage"):
        st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï du Camouflage, rendez-vous au :"))
        st.page_link("tomes/tome4/page_35.py", label="35", icon="📄")
    else:
        st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï du Camouflage, rendez-vous au :"))
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome4/page_35.py", label="35", icon="📄", disabled=True)

    if has_kai("Maîtrise Psychique de la Matière"):
        st.write_stream(stream_text("Si vous possédez la Discipline Kaï de la Maîtrise Psychique de la Matière, rendez-vous au :"))
        st.page_link("tomes/tome4/page_317.py", label="317", icon="📄")
    else:
        st.write_stream(stream_text("Si vous possédez la Discipline Kaï de la Maîtrise Psychique de la Matière, rendez-vous au :"))
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome4/page_317.py", label="317", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous ne maîtrisez aucune de ces deux Disciplines, il vous faudra attaquer le Garde par surprise. Rendez-vous au :"))
    if has_kai("Le Camouflage") or has_kai("Maîtrise Psychique de la Matière"):
        st.page_link("tomes/tome4/page_147.py", label="147", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome4/page_147.py", label="147", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
