import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, handle_repas, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=324, book=4)

fr_text = """
Vous avez faim et il vous faut prendre un Repas avant de vous
endormir, sinon vous perdrez 3 points d'ENDURANCE. Vous
dormez depuis environ deux heures, lorsque le son d'une cloche
vous réveille brusquement. « Des brigands ! s'écrie le tenancier
de la taverne. Ils sont entrés dans les écuries ! » Il vous faut
réagir immédiatement, sinon vos ennemis vous voleront vos
chevaux. Le tenancier vous indique qu'il existe deux moyens
d'accéder aux écuries. Vous pouvez soit sortir par la porte et
courir à l'extrémité du bâtiment, soit monter l'escalier jusqu'à un
balcon du premier étage d'où vous pourrez sauter sur le toit de
l'écurie.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    handle_repas()

    st.write_stream(stream_text("Si vous souhaitez passer par la porte, rendez-vous au :"))
    st.page_link("tomes/tome4/page_114.py", label="114", icon="📄")

    st.write_stream(stream_text("Si vous préférez sauter du balcon du premier étage, rendez-vous au :"))
    st.page_link("tomes/tome4/page_196.py", label="196", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
