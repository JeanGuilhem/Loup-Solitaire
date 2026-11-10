import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    pickup_gold,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=199, book=7)

fr_text = """
Vous reconnaissez le haubert de l'homme mort : c'est celui d'un
mercenaire Kakush. En effet, vous remarquez que chacune des
boucles rouillées qui forment sa cotte de mailles est ornée des dix
étoiles de Nikesa, symbole de la capitale de ce pays. Dans une
bourse en cuir attachée à sa ceinture, vous trouvez 6 Pièces d'Or
et, dans son Sac à Dos à moitié déchiré, une corde et un habit
rouge à capuchon. Vous examinez ensuite ses armes : elles sont
toutes deux hors d'usage. Le poignard à manche d'os tombe en
poussière lorsque vous essayez de l'arracher du crâne du cadavre,
et la lame de l'épée est rongée par la rouille et émoussée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_gold(6, key="or_199")
    pickup_button("CORDE", key="corde_199", label="Prendre la Corde")
    pickup_button("HABIT ROUGE", key="habit_199", label="Prendre l'Habit Rouge à capuchon")

    st.write_stream(stream_text("Si vous souhaitez continuer à avancer le long du tunnel, rendez-vous au :"))
    st.page_link("tomes/tome7/page_318.py", label="318", icon="📄")

    st.write_stream(stream_text("Si vous préférez gravir les marches pour inspecter la trappe ouverte, rendez-vous au :"))
    st.page_link("tomes/tome7/page_93.py", label="93", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
