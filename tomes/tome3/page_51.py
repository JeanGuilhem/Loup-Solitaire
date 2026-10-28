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

check_inventory(current_page_number=51, book=3)

fr_text = """
Vous sentez que les Loups Maudits sont profondément
endormis. Vous avez une chance de pouvoir passer devant eux,
de maîtriser le Barbare des Glaces et de refermer la porte de la
cellule avant qu'ils ne s'éveillent. Vous savez cependant que vous
courez là un grand risque et que vos chances de réussite sont
faibles.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous êtes suffisamment courageux pour entrer dans une cellule remplie de Loups Maudits, rendez-vous au :'))
    st.page_link("tomes/tome3/page_285.py", label="285", icon="📄")

    st.write_stream(stream_text("Si vous préférez ne pas prendre ce risque, il vous faut quitter les lieux et descendre l'escalier. Rendez-vous pour cela au :"))
    st.page_link("tomes/tome3/page_261.py", label="261", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
