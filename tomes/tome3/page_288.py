import streamlit as st
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

check_inventory(current_page_number=288, book=3)

fr_text = """
Cette nuit-là, une tempête souffle sur la banquise et enterre votre
tente sous la neige. Tandis que vous dormez, la toile fléchit sous
le poids de cette couche compacte et vient effleurer vos
Couvertures de Fourrure. Au matin, celles-ci sont trempées et,
lorsque vous vous réveillez, vos deux jambes sont paralysées par
de terribles crampes. Il vous faut les masser pendant presque
une heure avant que vous ne puissiez à nouveau vous tenir
debout. Vous souhaitez alors n'avoir jamais mis les pieds dans
cet enfer glacé.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome3/page_167.py", label="167", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
