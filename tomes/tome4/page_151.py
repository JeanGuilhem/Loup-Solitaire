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

check_inventory(current_page_number=151, book=4)

fr_text = """
Le sol du tunnel est couvert de restes décomposés de rongeurs.
Le bruit des os qui craquent sous les pas de vos hommes, à
mesure qu'ils avancent parmi ces débris pestilentiels, vous fait
grimacer de dégoût. Vous arrivez bientôt à un endroit où le
tunnel tourne brusquement vers l'est. La lumière d'une Torche se
reflète sur les murs de pierre brute. En jetant un coup d'œil à
l'angle du tunnel, vos soupçons se trouvent confirmés : deux
Guerriers vêtus d'armures montent en effet la garde devant un
puits qui s'enfonce dans le sol d'une salle éclairée par des
Torches.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez faire signe à vos hommes d'attaquer les Gardes, rendez-vous au :"))
    st.page_link("tomes/tome4/page_320.py", label="320", icon="📄")

    st.write_stream(stream_text('Si vous préférez attirer les Gardes dans le tunnel afin de les capturer vivants, rendez-vous au :'))
    st.page_link("tomes/tome4/page_197.py", label="197", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
