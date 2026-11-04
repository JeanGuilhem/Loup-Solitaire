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

check_inventory(current_page_number=327, book=5)

fr_text = """
Votre coup a transpercé le guerrier Drakkar ainsi que sa
monture. Le Kraan tombe en tournoyant, larguant son cavalier
dans sa chute. Alors que l'horrible cri de désespoir du Drakkar
retentit à vos oreilles, vous obliquez vers le sud pour éviter d'être
pris entre deux escadrons de Kraans qui convergent vers vous. Ce
brusque changement de direction augmente la distance qui vous
sépare de vos poursuivants, mais l'Itikar est grièvement blessé et
vous n'avez plus tellement d'espoir de vous en sortir vivant. En
effet, votre monture a perdu tellement de sang qu'elle peut
défaillir à tout moment et vous précipiter dans le vide, vers le lac
Inrahim. Mais soudain, vous apercevez quelque chose dans le
lointain, et cette vision vous redonne envie de croire aux miracles !
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome5/page_221.py", label="221", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
