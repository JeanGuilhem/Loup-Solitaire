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

check_inventory(current_page_number=73, book=6)

fr_text = """
Peu avant midi, vous traversez un village désert. Des
habitations en ruine et des fermes calcinées dressent leurs
sinistres vestiges sur votre passage. Vous constatez que la
guerre a étendu ses ravages jusqu'en ce coin reculé. Quelques
kilomètres plus loin, vous passez devant une chapelle se
dressant au bord de la route. Un homme, vêtu de loques et
couvert de boue, se déplace d'un pas incertain parmi les tombes
qui entourent l'édifice, en claudiquant comme un oiseau blessé.
Alors que vous approchez, l'homme se met à appeler au secours
d'une voix plaintive.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez lui venir en aide, rendez-vous au :"))
    st.page_link("tomes/tome6/page_337.py", label="337", icon="📄")

    st.write_stream(stream_text("Si vous préférez l'ignorer et poursuivre votre route vers Soren, rendez-vous au :"))
    st.page_link("tomes/tome6/page_191.py", label="191", icon="📄")

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de la Science Médicale, rendez-vous au :"))
    if has_magnakai("Science Médicale"):
        st.page_link("tomes/tome6/page_173.py", label="173", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome6/page_173.py", label="173", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
