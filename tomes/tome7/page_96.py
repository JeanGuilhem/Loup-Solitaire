import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=96, book=7)

fr_text = """
Au moment où vous soulevez l'épée du bloc de marbre, un cri
lugubre retentit : on dirait un loup hurlant à la lune. Votre cœur
fait un bond, et vous vous écartez vivement du socle, vous
attendant presque à le voir se changer en un monstre affamé.
Mais rien de tel ne se passe et vos frayeurs s'apaisent. Riant de
votre peur injustifiée, vous mettez votre nouvelle arme au
fourreau et vous réfléchissez à la direction que vous allez prendre
maintenant.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_button("ÉPÉE", key="epee", label="Mettre l'Épée au fourreau")

    st.write_stream(stream_text("Si vous voulez quitter la cave par le tunnel de gauche, rendez-vous au :"))
    st.page_link("tomes/tome7/page_48.py", label="48", icon="📄")

    st.write_stream(stream_text("Si vous préférez partir par le tunnel de droite, rendez-vous au :"))
    st.page_link("tomes/tome7/page_176.py", label="176", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
