import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    remove_from_inventory,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=157, book=3)

fr_text = """
Vous prenez la Potion dans votre Sac à Dos et vous entrebâillez
prudemment la porte, juste assez pour pouvoir vider la fiole dans
le chaudron bouillonnant. Quelques minutes plus tard, les
Barbares des Glaces tombent dans un profond sommeil juste
après avoir achevé leur repas. Vous pouvez à présent inspecter
les lieux. La cuisine est petite et elle contient une étonnante
provision d'herbes. « Ces herbes viennent du comptoir de
Liouk », assure Loi-Kymar en examinant attentivement les
étiquettes qui indiquent ce que les bocaux contiennent. Il remplit
ses poches de plusieurs de ces bocaux, puis il en ouvre deux
autres et mélange les herbes qu'ils renferment. Il vous tend
ensuite cette mixture : « Voici qui vous donnera des forces, Loup
Solitaire », dit-il. Vous mangez les feuilles séchées et, aussitôt,
une chaleur bienfaisante se répand dans tout votre corps. Vous
récupérez 6 points d'ENDURANCE.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        remove_from_inventory("POTION DE BROSSE À POTENCES")
        change_endurance(6)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=6)
    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome3/page_301.py", label="301", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
