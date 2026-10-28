import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=206, book=3)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Retenant à la fois votre souffle et votre matériel, vous essayez
d'atterrir le plus silencieusement possible sur le sol poussiéreux
du couloir. Malheureusement, vous vous tordez la cheville en
tombant et vous laissez échapper un cri de douleur. Vous perdez
1 point d'ENDURANCE. Vous apercevez alors avec horreur un
Barbare des Glaces assis à une dizaine de mètres de vous, sur
votre gauche. Il tourne lentement la tête dans votre direction
mais, en jetant un bref coup d'œil vers la droite, vous découvrez
un autre couloir orienté au nord, à moins de 5 mètres de l'endroit
où vous êtes agenouillé.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-1)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-1)
    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï du Camouflage, rendez-vous au :"))
    if has_kai("Le Camouflage"):
        st.page_link("tomes/tome3/page_74.py", label="74", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome3/page_74.py", label="74", icon="📄", disabled=True)
    st.write_stream(
        stream_text(
            "Sinon, vous pouvez essayer de courir en direction du couloir orienté au nord, en priant le ciel "
            "que le Barbare des Glaces ne vous voie pas. Rendez-vous pour cela au :"
        )
    )
    st.page_link("tomes/tome3/page_183.py", label="183", icon="📄")
    st.write_stream(
        stream_text(
            "Enfin, si vous préférez attaquer le Barbare pour tenter de le neutraliser avant qu'il ait pu "
            "donner l'alerte, rendez-vous au :"
        )
    )
    st.page_link("tomes/tome3/page_161.py", label="161", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
