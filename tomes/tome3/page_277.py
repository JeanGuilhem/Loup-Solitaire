import streamlit as st
from combat import combat_weapons
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=277, book=3)

fr_text = """
Vous vous enfuyez à toutes jambes en revenant sur vos pas, mais
les Languabarbs sont familiers des lieux et ils gagnent du terrain.
Lorsque vous atteignez la cascade gelée, vous remarquez qu'un
gros bloc rocheux aux couleurs argentées forme saillie au-dessus
de l'entrée de la grotte.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if combat_weapons():
        st.write_stream(stream_text('Si vous possédez une arme, vous pouvez essayer de faire tomber ce roc pour obstruer le passage ; rendez-vous pour cela au :'))
        st.page_link("tomes/tome3/page_142.py", label="142", icon="📄")
    else:
        st.write_stream(stream_text("Vous ne possédez aucune arme pour faire tomber ce roc."))
        st.page_link("tomes/tome3/page_142.py", label="142", icon="📄", disabled=True)
        st.write_stream(stream_text("Vous ne disposez d'aucune arme : vous devrez faire face aux créatures et les combattre ; rendez-vous alors au :"))
        st.page_link("tomes/tome3/page_32.py", label="32", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
