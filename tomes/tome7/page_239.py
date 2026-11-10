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

check_inventory(current_page_number=239, book=7)

fr_text = """
Vous entendez un craquement aigu, puis vous êtes violemment
projeté en l'air. Les pavés puants de la jetée saluent votre retour
sur terre, et vous effectuez instinctivement un roulé-boulé pour
amortir le choc. Vous restez le souffle coupé pendant un court
instant mais vous n'êtes pas blessé. Vous vous relevez tant bien
que mal, et apercevez deux escaliers rudimentaires au bout de la
jetée : l'un monte vers ce qui semble être l'entrée d'une grotte
creusée dans l'abrupte paroi rocheuse, l'autre descend vers une
petite plage de sable noir où pointent de gros rochers.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez grimper les marches jusqu'à l'entrée de la grotte, rendez-vous au :"))
    st.page_link("tomes/tome7/page_82.py", label="82", icon="📄")

    st.write_stream(stream_text("Si vous préférez descendre vers la plage, rendez-vous au :"))
    st.page_link("tomes/tome7/page_30.py", label="30", icon="📄")

    st.write_stream(stream_text("Enfin, si vous maîtrisez la Discipline Magnakaï de l'Exploration, rendez-vous au :"))
    if has_magnakai("Exploration"):
        st.page_link("tomes/tome7/page_251.py", label="251", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome7/page_251.py", label="251", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
