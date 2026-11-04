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

check_inventory(current_page_number=203, book=5)

fr_text = """
Un flot de sang vert s'écoule de l'habit rouge du Vordak en
dégageant une odeur acide et écœurante. La créature pousse un
cri, bascule, et son corps mutilé tombe en vrille dans les airs.
Vous rengainez votre arme, puis vous saisissez les rênes et vous
tentez de reprendre le contrôle de votre monture blessée. Vous
avez tué le Vordak, mais la bataille n'est pas encore gagnée car
l'Itikar perd beaucoup de sang et peut sombrer dans
l'inconscience à tout moment en vous laissant choir comme une
pierre vers le lac Inrahim. Tout à coup, vous apercevez quelque
chose au loin, quelque chose qui vous redonne foi dans les
miracles.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_221.py", label="221", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
