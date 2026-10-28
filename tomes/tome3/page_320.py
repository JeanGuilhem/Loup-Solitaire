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

check_inventory(current_page_number=320, book=3)

fr_text = """
Vous parvenez à immobiliser l'enfant et à ôter de sa botte un
poignard en os qu'il cherchait à atteindre pour vous frapper dans
le dos. Les Barbares des Glaces, pendant ce temps, vous ont
encerclé, mais ils n'osent pas vous attaquer tant que vous tenez
un de leurs enfants en otage.
Le poignard en os appuyé contre la gorge du jeune garçon, vous
vous approchez prudemment du traîneau, mais vous vous rendez
bientôt compte que vous ne parviendrez pas à distancer vos
poursuivants sur un traîneau chargé. Il va falloir prendre
rapidement une décision.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez débarrasser le traîneau de son chargement, libérer l'enfant Barbare et vous enfuir sur le traîneau ainsi allégé, rendez-vous au :"))
    st.page_link("tomes/tome3/page_190.py", label="190", icon="📄")
    st.write_stream(stream_text("Si vous préférez vous débarrasser du chargement mais garder l'enfant en otage au cours de votre fuite, rendez-vous au :"))
    st.page_link("tomes/tome3/page_33.py", label="33", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
