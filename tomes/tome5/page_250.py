import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=250, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Tandis que vous regardez les Kraans et leurs cavaliers disparaître
dans le ciel obscurci, un grondement de tonnerre retentit au-dessus de Barrakeesh et roule à travers la plaine. Ce bruit
inquiétant est lourd de menace, comme si la ville elle-même
maudissait votre fuite. Vous vous détournez et vous concentrez
votre attention sur Banedon, votre sauveur inattendu. Celui-ci
est livide et le pansement de fortune qui entoure sa blessure est
trempé de sang.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï de la Guérison, rendez-vous au :"))
    if has_kai("La Guérison"):
        st.page_link("tomes/tome5/page_377.py", label="377", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_377.py", label="377", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous ne maîtrisez pas cette Discipline, rendez-vous au :"))
    if has_kai("La Guérison"):
        st.page_link("tomes/tome5/page_339.py", label="339", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome5/page_339.py", label="339", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
