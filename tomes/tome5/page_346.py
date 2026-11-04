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

check_inventory(current_page_number=346, book=5)

fr_text = """
Sur le côté de la rue, un vieillard vend tout un assortiment de
carpettes et de tapis, empilés à l'arrière d'une charrette. Banedon
s'approche de lui et ils discutent tous deux pendant plusieurs minutes.
Finalement, le jeune sorcier tend au vieil homme un anneau et le
visage ridé du marchand s'illumine de joie tandis que Banedon
revient vers vous, porteur de bonnes nouvelles. « Retournons
vers la ruelle que nous avons croisée il y a quelque temps ; c'est là
que demeure Tipasa, dans la maison à la porte bleue qui se
trouve tout au bout. » Tandis que vous retournez sur vos pas et
que vous pénétrez dans la ruelle sombre et malpropre, vous
entendez le marchand pousser un cri de déception : l'anneau
vient de se volatiliser à son doigt. Arrivés au bout de la ruelle,
vous trouvez enfin la maison à la porte bleue.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome5/page_206.py", label="206", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
