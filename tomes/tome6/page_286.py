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

check_inventory(current_page_number=286, book=6)

fr_text = """
Vous courez jusqu'à une échelle, poursuivi par le pirate. Vous
évitez de justesse la lame tranchante de son couteau qui débite
les barreaux de bois sous vos pieds au fur et à mesure que vous
grimpez. Finalement, vous parvenez à vous hisser sur le pont
principal et vous apercevez, à l'autre bout du bateau, un des
hommes de l'équipage en train de se battre avec un pirate. Ce
dernier, sec et nerveux, prend rapidement le dessus et achève le
marin d'un coup de couteau ; il vous aperçoit alors et tire une
nouvelle lame de la série de poignards qu'il porte accrochés en
travers de la poitrine. Le pont n'offre aucun abri. Le pirate lève
son bras, prêt à lancer son arme.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de l'Art de la Chasse, rendez-vous au :"))
    if has_magnakai("Art de la Chasse"):
        st.page_link("tomes/tome6/page_314.py", label="314", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome6/page_314.py", label="314", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous ne maîtrisez pas cette Discipline, rendez-vous au :"))
    if not has_magnakai("Art de la Chasse"):
        st.page_link("tomes/tome6/page_142.py", label="142", icon="📄")
    else:
        st.page_link("tomes/tome6/page_142.py", label="142", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
