import streamlit as st
from inventory import (
    can_shoot,
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=69, book=7)

fr_text = """
A l'intérieur de la pièce où vous pénétrez, les créatures vêtues de
pourpre que vous aviez entr'aperçues auparavant se lèvent de
table en hurlant et pointent leurs longs doigts sur vous d'un air
accusateur. Dans la seconde qui suit, une cloche d'alarme retentit
dans tout le couloir et des gardes en uniforme noir, identiques à
ceux que vous avez déjà rencontrés, font irruption par le passage
voûté, l'épée au poing et la visière baissée, prêts au combat. Dès
qu'ils vous aperçoivent, ils se ruent sur vous avec frénésie.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez un arc, et si vous voulez vous en servir, rendez-vous au :"))
    st.page_link("tomes/tome7/page_50.py", label="50", icon="📄", disabled=not (can_shoot()))

    st.write_stream(stream_text("Si vous préférez vous défendre avec une arme à main, rendez-vous au :"))
    st.page_link("tomes/tome7/page_316.py", label="316", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
