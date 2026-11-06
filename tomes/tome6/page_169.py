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

check_inventory(current_page_number=169, book=6)

fr_text = """
La porte en fer n'est pas verrouillée, mais vous constatez avec
horreur que ses gonds sont tellement rouillés qu'elle ne bougera
pas d'un pouce. Soudain, le Yamsark surgit en haut de l'escalier,
reniflant et glapissant d'une effroyable façon. Il vous fixe
cruellement de ses yeux rouges et se prépare à bondir.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # Cercle du Feu = Science des Armes + Art de la Chasse
    fire_circle = has_magnakai("Science des Armes") and has_magnakai("Art de la Chasse")
    st.write_stream(stream_text("Si vous avez complété le Cercle du Feu (c'est-à-dire si vous maîtrisez les deux Disciplines Magnakaï de la Science des Armes et de l'Art de la Chasse), rendez-vous au :"))
    if fire_circle:
        st.page_link("tomes/tome6/page_65.py", label="65", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome6/page_65.py", label="65", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous ne maîtrisez pas ces deux disciplines, mais que vous voulez, malgré tout, vous préparer à combattre, rendez-vous au :"))
    st.page_link("tomes/tome6/page_222.py", label="222", icon="📄", disabled=fire_circle)

    st.write_stream(stream_text("Si vous jugez plus prudent de partir en courant et de vous enfoncer plus profondément dans les ruines, rendez-vous au :"))
    st.page_link("tomes/tome6/page_285.py", label="285", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
