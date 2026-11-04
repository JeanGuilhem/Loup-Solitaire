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

check_inventory(current_page_number=75, book=5)

fr_text = """
Vous actionnez la poignée, mais la porte est fermée à clé. Vous
êtes sur le point de faire demi-tour et de repartir en courant,
quand la porte s'ouvre soudainement. Un homme apparaît dans
l'encadrement et vous chuchote : « Entrez vite, Homme du Nord,
je vous cacherai. » Puis il s'efface pour vous laisser passer.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez entrer, rendez-vous au :"))
    st.page_link("tomes/tome5/page_24.py", label="24", icon="📄")

    st.write_stream(stream_text("Si vous préférez décliner l'offre de cet homme et remonter la rue qui mène au porche, rendez-vous au :"))
    st.page_link("tomes/tome5/page_169.py", label="169", icon="📄")

    st.write_stream(stream_text("Si enfin vous voulez emprunter l'allée, rendez-vous au :"))
    st.page_link("tomes/tome5/page_117.py", label="117", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
