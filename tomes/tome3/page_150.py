import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_flag,
    has_item,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

fr_unknown_item = "Vous ne possédez pas cet objet."

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=150, book=3)

fr_text = """
Le coup que vous assénez fracasse la surface lisse et blanche de la
Statue. Aussitôt une rafale de vent glacé s'échappe en sifflant de
l'ouverture et, quelques secondes plus tard, tous les murs de la
salle sont recouverts d'une couche de glace étincelante. La chute
soudaine de la température vous fait perdre 2 points
d'ENDURANCE, à moins que votre peau ne soit protégée par de
l'huile de Bakanal. Vous constatez alors avec un sentiment
d'horreur que la rafale de vent prend peu à peu la forme d'un
petit cyclone qui attire dans son œil tous les morceaux de pierre
et de glace traînant alentour. Vous venez de libérer un Démon de
Glace et cette terrifiante créature a l'intention de vous anéantir.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if has_flag("huile de Bakanal"):
        st.success("*L'huile de Bakanal dont vous êtes enduit vous protège du froid.*")
    else:
        if is_new_page():
            change_endurance(-2)
        st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)
    st.write_stream(stream_text("Si vous disposez du Glaive de Sommer, rendez-vous immédiatement au :"))
    if has_item("GLAIVE DE SOMMER"):
        st.page_link("tomes/tome3/page_120.py", label="120", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome3/page_120.py", label="120", icon="📄", disabled=True)
    st.write_stream(stream_text("Si vous souhaitez attaquer le cyclone avec une arme normale, rendez-vous au :"))
    st.page_link("tomes/tome3/page_18.py", label="18", icon="📄")
    st.write_stream(stream_text("Si vous préférez essayer de vous enfuir en courant vers l'arcade, rendez-vous au :"))
    st.page_link("tomes/tome3/page_211.py", label="211", icon="📄")
    st.write_stream(stream_text("Enfin, si vous possédez une Sphère de Feu, rendez-vous au :"))
    if has_item("SPHÈRE DE FEU"):
        st.page_link("tomes/tome3/page_310.py", label="310", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome3/page_310.py", label="310", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
