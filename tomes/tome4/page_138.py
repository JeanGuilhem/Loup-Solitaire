import streamlit as st
from combat import combat
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

check_inventory(current_page_number=138, book=4)

fr_text = """
Vous êtes arrivé au milieu de la rampe lorsqu'un Garde se tourne
pour vous faire face. Il bat des paupières et frotte ses yeux
injectés de sang d'un air incrédule. Profitant de l'effet de
surprise, vous vous précipitez sur lui en espérant pouvoir le
frapper avant qu'il n'ait pleinement réalisé la situation. Alors
qu'il s'apprête à pousser un cri, vous lui portez un coup qui le
précipite par-dessus le bord de la rampe. L'autre Garde tire son
épée et se relève tant bien que mal. De toute évidence il est ivre et
rendu fou furieux par votre attaque. Il se rue alors sur vous
comme un chien enragé.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("GARDE IVRE", 13, 29)], flee_after=0)
    if outcome == "fled":
        st.write_stream(stream_text('Vous pouvez prendre la fuite à tout moment en courant dans le tunnel situé à ce niveau. Rendez-vous pour cela au :'))
        st.page_link("tomes/tome4/page_81.py", label="81", icon="📄")
    elif outcome == "win":
        st.write_stream(stream_text('Si vous remportez la victoire, rendez-vous au :'))
        st.page_link("tomes/tome4/page_152.py", label="152", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
