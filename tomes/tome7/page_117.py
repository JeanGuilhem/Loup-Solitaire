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

check_inventory(current_page_number=117, book=7)

fr_text = """
Malheureusement, les rats ne craignent pas l'eau et ils
s'acharnent sur vous tandis que vous poussez votre canot dans
les eaux froides du lac. Vous vous hissez rapidement dans la frêle
embarcation, puis vous vous débarrassez à grands coups des
rongeurs les plus tenaces, avant de vous éloigner vers le large.
Vous avez à peine ramé plus de cent mètres lorsque vous
constatez que le bateau penche dangereusement sur un côté. Les
rats ont rongé la coque, en dessous de la ligne de flottaison, et
vous êtes tout simplement en train de couler !
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de la Science Médicale, rendez-vous au :"))
    if has_magnakai("Science Médicale"):
        st.page_link("tomes/tome7/page_234.py", label="234", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome7/page_234.py", label="234", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous ne maîtrisez pas cette discipline, ou si vous ne souhaitez pas y recourir, rendez-vous au :"))
    st.page_link("tomes/tome7/page_325.py", label="325", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
