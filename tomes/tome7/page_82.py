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

check_inventory(current_page_number=82, book=7)

fr_text = """
Tandis que vous gravissez les marches dangereusement
glissantes, un coup de tonnerre éclate dans le lointain, et
quelques gouttes de pluie s'écrasent sur la capuche de votre
manteau Kaï. A n'en pas douter, un violent orage se prépare. Au
moment où vous atteignez l'entrée de la grotte, une terrible rafale
de vent vient fouetter la paroi rocheuse ; le sol tout entier vibre
sous l'effet des coups de tonnerre de plus en plus rapprochés,
suivis de près par d'impressionnants éclairs de lumière verte.
Mais alors que vous vous apprêtez à pénétrer dans la grotte, des
relents pestilentiels vous prennent à la gorge. Malgré votre désir
de vous mettre à l'abri, la puanteur qui se dégage de cet endroit
vous fait quelque peu hésiter.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de l'Exploration, rendez-vous au :"))
    if has_magnakai("Exploration"):
        st.page_link("tomes/tome7/page_65.py", label="65", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome7/page_65.py", label="65", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous voulez entrer dans la grotte, rendez-vous au :"))
    st.page_link("tomes/tome7/page_277.py", label="277", icon="📄")

    st.write_stream(stream_text("Si vous préférez ne pas vous y risquer, il ne vous reste pas d'autre solution que de redescendre l'escalier et retourner sur la plage ; rendez-vous, dans ce cas, au :"))
    st.page_link("tomes/tome7/page_30.py", label="30", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
