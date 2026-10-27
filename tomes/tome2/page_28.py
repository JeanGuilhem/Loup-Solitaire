import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=28, book=2)

fr_text = """
Les Squalls se mettent à hurler de terreur et s'enfuient en tous sens pour
éviter vos coups. En quelques instants, ils ont déserté la clairière et
vous vous approchez du moribond pour lui porter secours. Il lui reste
tout juste un souffle de vie et il est bien entendu beaucoup trop faible
pour parler.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez retirer avec précaution la lance de sa poitrine, rendez-vous au :"))
    st.page_link("tomes/tome2/page_106.py", label="106", icon="📄")
    st.write_stream(stream_text("Si vous préférez fouiller dans son sac dans l'espoir d'y trouver quelque objet qui pourrait se révéler utile, rendez-vous au :"))
    st.page_link("tomes/tome2/page_320.py", label="320", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
