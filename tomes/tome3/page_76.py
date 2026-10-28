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

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=76, book=3)

fr_text = """
Vous continuez à monter des marches jusqu'à ce que vous
arriviez devant une étroite porte de pierre. Comme toutes les
autres portes que vous avez vues jusqu'à présent, celle-ci est
également actionnée par un levier fixé au mur. Un petit judas a
été aménagé au milieu de la porte. Avec prudence, vous collez un
œil contre cette minuscule ouverture et vous jetez un regard dans
la petite pièce située derrière. Vous apercevez alors trois Loups
Maudits endormis sur le sol de cette cellule. La porte d'une autre
cellule s'ouvre dans le mur nord et vous apercevez, se découpant
dans l'embrasure, la silhouette d'un Barbare des Glaces qui vous
tourne le dos.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous maîtrisez la Discipline Kaï de la Chasse ou celle de la Communication Animale, rendez-vous au :'))
    if has_kai("La Chasse") or has_kai("Communication Animale"):
        st.page_link("tomes/tome3/page_51.py", label="51", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome3/page_51.py", label="51", icon="📄", disabled=True)

    st.write_stream(stream_text('Si vous ne possédez aucune de ces deux Disciplines, vous pouvez ouvrir la porte et attaquer les Loups Maudits en vous rendant au :'))
    st.page_link("tomes/tome3/page_137.py", label="137", icon="📄", disabled=has_kai("La Chasse") or has_kai("Communication Animale"))

    st.write_stream(stream_text("Si vous préférez vous éloigner de la porte de cette cellule, redescendez l'escalier en vous rendant au :"))
    st.page_link("tomes/tome3/page_261.py", label="261", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
