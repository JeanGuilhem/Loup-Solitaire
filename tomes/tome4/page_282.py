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

check_inventory(current_page_number=282, book=4)

fr_text = """
La serrure est rouillée et grippée, mais elle finit par céder et la
porte s'ouvre. Vous pénétrez alors dans un étroit passage qui
descend vers une autre porte située 15 mètres plus loin. Vous
donnez l'ordre à vos hommes de partir en avant tandis que vous
refermez la porte. Vous éprouvez de grandes difficultés à
actionner à nouveau la serrure pour verrouiller le panneau.
Lorsque vous entendez enfin cliqueter le mécanisme, un autre
cliquetis, beaucoup plus sonore, retentit comme un écho : une
trappe vient de s'ouvrir dans le sol au beau milieu du passage.
Tous vos hommes, hurlant de terreur, sont alors précipités dans
un gouffre profond. La gorge nouée par la peur, vous vous
approchez du bord du gouffre et vous scrutez ses profondeurs
obscures. Les parois de la fosse sont verticales et vous ne
parvenez pas à en distinguer le fond. Un courant d'air froid et le
sifflement sinistre d'un vent lointain montent du gouffre. Il n'y a
plus rien à faire, il ne vous reste plus qu'à adresser un adieu
silencieux à vos hommes perdus à jamais. Le cœur lourd, vous
contournez le gouffre et vous vous dirigez vers l'autre porte, au
bout du passage.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_257.py", label="257", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
