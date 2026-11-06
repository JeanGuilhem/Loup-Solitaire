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

check_inventory(current_page_number=301, book=6)

fr_text = """
D'un mouvement rapide et élégant, qui vous désigne comme
étant un Maître Kaï, vous prenez une flèche dans votre carquois,
tendez la corde de votre Arc et visez. La flèche transperce l'avant-
bras du jeune seigneur au moment où il allait frapper. Il pousse
un cri strident, laisse tomber son épée, puis tombe à la renverse
en se tenant le bras. « Sois maudit, sale chacal ! crie-t-il. Je suis
Roark, noble d'Amory, je me vengerai, je t'en donne ma parole ! »
Tremblant de douleur et de fureur, il se relève et demande son
manteau et son épée au tavernier avant de disparaître dans la
nuit sous une bordée d'injures.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome6/page_281.py", label="281", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
