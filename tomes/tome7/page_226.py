import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=226, book=7)

fr_text = """
Tout à coup, sans que rien ne le laisse présager, la main s'anime
et se dresse à la verticale en prenant appui sur trois de ses doigts,
les deux autres repliés en arrière. La main ressemble ainsi à une
monstrueuse araignée, prête à attaquer. Vous reculez, terrifié,
tandis qu'elle tourne rapidement sur le socle de granit.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez attaquer la main, rendez-vous au :"))
    st.page_link("tomes/tome7/page_116.py", label="116", icon="📄")

    st.write_stream(stream_text("Si vous avez une Graine de Feu et que vous voulez la jeter sur le socle, rendez-vous au :"))
    st.page_link("tomes/tome7/page_157.py", label="157", icon="📄", disabled=not has_item("GRAINE DE FEU"))

    st.write_stream(stream_text("Enfin, si vous préférez contourner le socle pour entrer dans le passage qui se trouve de l'autre côté, rendez-vous au :"))
    st.page_link("tomes/tome7/page_302.py", label="302", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
