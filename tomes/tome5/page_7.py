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

check_inventory(current_page_number=7, book=5)

fr_text = """
Vous relâchez la corde de l'arc et la flèche fend l'air en direction
de votre cible. Cependant, vous avez mal évalué la distance et la
flèche n'atterrit pas assez loin : elle se brise sur les pavés du port,
révélant ainsi aux hommes de Maouk l'endroit où vous vous
trouvez. Vous vous apprêtez à prendre la fuite, mais la frêle
embarcation est rapidement encerclée par vos ennemis et vous
êtes contraint de vous rendre. Tandis que les Sharnazims tout de
noir vêtus vous traînent le long du quai, vous redoutez que votre
dernière heure ne soit arrivée...
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome5/page_176.py", label="176", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
