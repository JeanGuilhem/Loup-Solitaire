import streamlit as st
from inventory import (
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

check_inventory(current_page_number=150, book=5)

fr_text = """
Le couloir va vers le nord, mais il aboutit bientôt à un croisement
d'où part un autre passage orienté est-ouest. Prudemment, vous
regardez à droite et à gauche mais vous ne voyez aucune
sentinelle. A l'est, vous distinguez un escalier qui descend à perte
de vue. A l'ouest, vous apercevez une porte fermée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez aller vers l'est, vers cet escalier, rendez-vous au :"))
    st.page_link("tomes/tome5/page_93.py", label="93", icon="📄")

    st.write_stream(stream_text("Si vous préférez aller vers l'ouest, en direction de la porte, rendez-vous au :"))
    st.page_link("tomes/tome5/page_122.py", label="122", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
