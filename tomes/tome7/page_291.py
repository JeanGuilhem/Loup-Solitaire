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

check_inventory(current_page_number=291, book=7)

fr_text = """
Un terrible gémissement retentit dans le tunnel au moment où
vous blessez un des doigts de la main monstrueuse. Aussitôt, les
autres s'ouvrent, relâchant Tavig qui tombe sur le sol comme une
masse. Tandis que la main se retire dans l'obscurité, vous vous
agenouillez à côté du corps ensanglanté de votre compagnon et
vous essayez de l'aider du mieux que vous pouvez, mais ses
blessures sont graves : il est à l'article de la mort.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    healer = has_magnakai("Science Médicale")
    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de la Science Médicale, rendez-vous au :"))
    if healer:
        st.page_link("tomes/tome7/page_133.py", label="133", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome7/page_133.py", label="133", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous ne maîtrisez pas cette discipline, rendez-vous au :"))
    st.page_link("tomes/tome7/page_125.py", label="125", icon="📄", disabled=healer)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
