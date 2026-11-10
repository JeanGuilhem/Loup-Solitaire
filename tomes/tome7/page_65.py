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

check_inventory(current_page_number=65, book=7)

fr_text = """
Vous avez la nette impression que l'entrée recèle un traquenard.
L'odeur écœurante que vous sentez vous rappelle votre première
partie de chasse au pied des monts Durncrag, dans votre
Sommerlund natal, lorsque vous n'étiez encore qu'un Initié dans
la hiérarchie Kaï. Vous aviez, par hasard, découvert un ancien
antre d'ours qui abritait un nid de vipères des marais. La
puanteur qui se dégageait de ce cloaque était identique à celle
que vous respirez maintenant.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez entrer dans la grotte, rendez-vous au :"))
    st.page_link("tomes/tome7/page_258.py", label="258", icon="📄")

    st.write_stream(stream_text("Si vous préférez retourner sur la plage, rendez-vous au :"))
    st.page_link("tomes/tome7/page_30.py", label="30", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
