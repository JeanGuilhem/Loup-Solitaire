import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    show_illustrations,
    show_map,
)
from text import fr_unknown_magnakai
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=63, book=7)

fr_text = """
Vous vous ramassez sur vous-même dans le plus grand silence,
les nerfs à vif et les muscles bandés, dans l'attente d'une lutte
imminente. Soudain, vous percevez un nouveau bruit ; il ne
provient pas de la chambre, mais du tunnel même où vous êtes
caché. On dirait le craquement d'un œuf qui éclôt... En vous
retournant, vous voyez une multitude de serpents gluants, de la
taille d'un bras environ, qui sortent en frétillant des coquilles
d'œufs brisés. Ils se mettent instinctivement à ramper vers vous,
attirés par la chaleur de votre corps et poussés par une faim
dévorante.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    invisible = has_magnakai("Invisibilité")
    animal = has_magnakai("Contrôle Animal")
    st.write_stream(stream_text("Si vous possédez la Discipline Magnakaï de l'Invisibilité, rendez-vous au :"))
    if invisible:
        st.page_link("tomes/tome7/page_281.py", label="281", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome7/page_281.py", label="281", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous possédez la Discipline Magnakaï du Contrôle Animal, rendez-vous au :"))
    if animal:
        st.page_link("tomes/tome7/page_210.py", label="210", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome7/page_210.py", label="210", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous ne maîtrisez aucune de ces disciplines, rendez-vous au :"))
    st.page_link("tomes/tome7/page_178.py", label="178", icon="📄", disabled=invisible or animal)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
