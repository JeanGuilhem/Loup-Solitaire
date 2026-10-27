import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=334, book=2)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Quelques kilomètres plus loin, le sentier est recouvert de broussailles et
disparaît complètement sous les herbes et les buissons d'épines. Il
devient difficile d'avancer car les marécages et les fondrières abondent
sur la lande. Il vous faut plusieurs heures d'un parcours malaisé pour
atteindre enfin la lisière de la forêt de Durenor. Vous distinguez alors la
silhouette d'une haute tour dressée parmi les fougères. Des volutes de
fumée s'élèvent paresseusement d'une cheminée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez entrer dans cette tour, rendez-vous au :"))
    st.page_link("tomes/tome2/page_115.py", label="115", icon="📄")
    st.write_stream(stream_text("Si vous préférez chercher un chemin qui traverse la forêt, rendez-vous au :"))
    st.page_link("tomes/tome2/page_291.py", label="291", icon="📄")
    st.write_stream(stream_text("Enfin, si vous maîtrisez la Discipline Kaï de l'Orientation, rendez-vous au :"))
    if has_kai("L'Orientation"):
        st.page_link("tomes/tome2/page_98.py", label="98", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome2/page_98.py", label="98", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
