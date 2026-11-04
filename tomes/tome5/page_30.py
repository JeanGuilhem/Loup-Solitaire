import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    kai_rank,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=30, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Vous passez sous plusieurs arcades dont les voûtes élevées
dominent la muraille est de la ville, puis vous continuez à
avancer sans incident. Soudain des bruits de voix vous
parviennent. Les exclamations de Gardes affamés, ainsi que le
tintement caractéristique d'assiettes et de verres qu'on entrechoque vous informent qu'il y a dans les parages une
cantine pleine de soldats. Alors que vous réfléchissez à ce que
vous allez faire, une patrouille de Gardes apparaît brusquement
derrière vous, au fond du couloir. D'un bond, vous sautez sur le
rebord d'une fenêtre et vous vous aplatissez dans l'encadrement.
Néanmoins, vous savez que cette cachette est précaire et que les
Gardes ne manqueront sûrement pas de vous repérer en arrivant
à votre hauteur.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous désirez vous réfugier à l'extérieur, sur l'étroite corniche qui longe le mur du Palais, rendez-vous au :"))
    st.page_link("tomes/tome5/page_152.py", label="152", icon="📄")
    st.write_stream(stream_text('Si vous préférez attaquer les Gardes au moment où ils passeront devant vous, rendez-vous au :'))
    st.page_link("tomes/tome5/page_124.py", label="124", icon="📄")
    st.write_stream(stream_text('Si vous possédez le titre de Gardien Kaï, ou un titre supérieur, rendez-vous au :'))
    if kai_rank() >= 7:
        st.page_link("tomes/tome5/page_62.py", label="62", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_62.py", label="62", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
