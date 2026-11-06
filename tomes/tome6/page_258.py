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

check_inventory(current_page_number=258, book=6)

fr_text = """
Quelqu'un tire le verrou, et la grande porte s'ouvre lentement. «
Enfin, Esmond ! Est-ce que nous avons interrompu ta... » Cyrilus
s'étrangle au milieu de la phrase, les yeux écarquillés par la
surprise. Juste derrière la porte se tient un guerrier vêtu d'une
armure noir et or, monté sur un grand destrier. Il tient une
arbalète posée sur l'avant-bras et pointée dans votre direction.
Soudain, sans aucun avertissement, il presse la gâchette et le
carreau part en sifflant vers votre poitrine.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de l'Intuition, rendez-vous au :"))
    if has_magnakai("Intuition"):
        st.page_link("tomes/tome6/page_283.py", label="283", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome6/page_283.py", label="283", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de l'Art de la Chasse, rendez-vous au :"))
    if has_magnakai("Art de la Chasse"):
        st.page_link("tomes/tome6/page_164.py", label="164", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome6/page_164.py", label="164", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous ne maîtrisez aucune de ces disciplines, rendez-vous au :"))
    if not (has_magnakai("Intuition") or has_magnakai("Art de la Chasse")):
        st.page_link("tomes/tome6/page_97.py", label="97", icon="📄")
    else:
        st.page_link("tomes/tome6/page_97.py", label="97", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
