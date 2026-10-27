import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=6, book=2)

fr_text = """
Le garçon a remarqué que vous le suiviez et dès qu'il est sorti, il tourne
le coin du bâtiment et se met à courir en direction du sud. Vous vous
lancez à sa poursuite, mais il a tôt fait de disparaître dans le dédale des
allées qui longent les entrepôts du port. Vous vous dirigez vers l'est en
empruntant la rue du Col Vert et vous passez devant une autre entrée du
magasin. Un peu plus loin, vous remarquez une enseigne au-dessus de
la porte d'une petite boutique. On peut y lire l'inscription suivante :
MEKI MAJENOR MAÎTRE ARMURIER
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez entrer dans cette boutique, rendez-vous au :"))
    st.page_link("tomes/tome2/page_266.py", label="266", icon="📄")
    st.write_stream(stream_text("Si vous préférez poursuivre votre chemin en direction de l'est, rendez-vous au :"))
    st.page_link("tomes/tome2/page_310.py", label="310", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
