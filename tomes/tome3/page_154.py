import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=154, book=3)

fr_text = """
Votre jambe droite est blessée ; la plaie saigne abondamment, et
il semble que l'hémorragie ne s'arrêtera pas d'elle-même ; vous
posez donc un garrot de fortune autour de votre cuisse, puis vous
vous relevez tant bien que mal et vous jetez un coup d'œil
alentour. Ce monolithe, de toute évidence, avait pour fonction
d'empêcher les intrus de passer, ou de les prendre au piège. C'est
sans doute un mage qui, jadis, l'a ainsi doté d'un puissant
pouvoir d'explosion. Vous remarquez alors qu'un panneau s'est
ouvert dans le mur nord, découvrant un passage obscur qui
permet de quitter cette salle.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez explorer ce nouveau couloir, rendez-vous au :'))
    st.page_link("tomes/tome3/page_145.py", label="145", icon="📄")
    st.write_stream(stream_text("Si vous préférez essayer d'ouvrir à nouveau la porte par laquelle vous êtes entré, rendez-vous au :"))
    st.page_link("tomes/tome3/page_242.py", label="242", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
