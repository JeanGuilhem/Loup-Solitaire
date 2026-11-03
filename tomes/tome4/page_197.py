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

check_inventory(current_page_number=197, book=4)

fr_text = """
Vous lancez une pierre dans le tunnel pour attirer l'attention des
Gardes. Votre tactique réussit : quelques secondes plus tard,
vous entendez des pas s'approcher et vous vous lancez à
l'attaque. Vos hommes surgissant de l'obscurité n'ont aucun mal
à maîtriser leurs adversaires qu'ils désarment avant de leur lier
les mains. Les Gardes sont ensuite ramenés dans la salle où se
trouve le puits de mine.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez fouiller ces hommes, rendez-vous au :'))
    st.page_link("tomes/tome4/page_268.py", label="268", icon="📄")

    st.write_stream(stream_text("Si vous préférez les interroger d'abord, rendez-vous au :"))
    st.page_link("tomes/tome4/page_76.py", label="76", icon="📄")

    st.write_stream(stream_text('Enfin, si vous estimez plus opportun de les abandonner là et de poursuivre votre chemin, rendez-vous au :'))
    st.page_link("tomes/tome4/page_64.py", label="64", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
