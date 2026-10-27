import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    has_kai,
    show_illustrations,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=328, book=2)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."
fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
Deux Zombies essaient de vous interdire le passage, mais vous leur
tranchez le corps à tous deux d'un seul coup du Glaive de Sommer.
Vous vous trouvez à présent au pied de la tour et vous apercevez au-
dessus de vous la silhouette d'un homme bossu, vêtu d'une robe écarlate
et coiffé d'un tokmor, un turban de magicien, sur lequel l'image d'un
serpent a été brodée. L'homme tient un bâton noir dans sa main droite.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez un Pendentif avec une Étoile de Cristal, rendez-vous au :"))
    if has_item("PENDENTIF À L'ÉTOILE DE CRISTAL"):
        st.page_link("tomes/tome2/page_113.py", label="113", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome2/page_113.py", label="113", icon="📄", disabled=True)
    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï de l'Orientation, rendez-vous au :"))
    if has_kai("L'Orientation"):
        st.page_link("tomes/tome2/page_204.py", label="204", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome2/page_204.py", label="204", icon="📄", disabled=True)
    st.write_stream(stream_text("Si vous souhaitez monter en haut de la tour pour attaquer le bossu, rendez-vous au :"))
    st.page_link("tomes/tome2/page_73.py", label="73", icon="📄")
    st.write_stream(stream_text("Si vous préférez vous enfuir de ce vaisseau en sautant par-dessus bord, rendez-vous au :"))
    st.page_link("tomes/tome2/page_267.py", label="267", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
