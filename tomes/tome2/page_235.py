import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=235, book=2)

fr_text = """
Lorsque vous atteignez le palier de l'étage suivant, la porte cède dans
un grand fracas et la populace déchaînée entre en force. En haut des
marches, un Sabre est accroché à côté d'une cheminée. Vous pouvez
vous emparer de cette arme si vous le désirez. En jetant ensuite un coup
d'œil autour de vous, vous vous apercevez qu'il n'y a qu'un seul moyen
de sortir d'ici : sauter par la fenêtre pour atterrir sur la chaussée en
contrebas.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_button("SABRE", key="sabre", label="Prendre le Sabre")

    st.write_stream(stream_text('Si vous souhaitez sauter par la fenêtre, rendez-vous au :'))
    st.page_link("tomes/tome2/page_132.py", label="132", icon="📄")

    st.write_stream(stream_text("Si vous préférez affronter la populace qui monte l'escalier, rendez-vous au :"))
    st.page_link("tomes/tome2/page_90.py", label="90", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
