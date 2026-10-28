import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=340, book=3)

fr_text = """
Vous traînez les cadavres hors de la cuisine et vous les
abandonnez derrière la porte secrète. Lorsque vous revenez, Loi-
Kymar est occupé à examiner les bocaux remplis d'herbes qui
sont alignés sur les étagères. Il prend plusieurs de ces bocaux
qu'il range dans ses poches, puis il en ouvre deux autres dont il
mélange le contenu dans un petit bol de pierre. Il vous tend
ensuite une poignée d'herbes sèches en vous conseillant de les
manger. « Elles vous rendront vos forces, Loup Solitaire», dit-il.
Vous mangez les herbes au goût douceâtre et une chaleur
bienfaisante rayonne aussitôt dans tout votre corps. Vous pouvez
ajouter 6 points d'ENDURANCE à votre total actuel.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(6)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=6)
    st.write_stream(stream_text("Rendez-vous à présent au :"))
    st.page_link("tomes/tome3/page_301.py", label="301", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
