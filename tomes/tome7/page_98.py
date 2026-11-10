import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=98, book=7)

fr_text = """
Vous contournez prudemment le trône, l'arme à la main et prêt à
toute éventualité. Mais lorsque vous arrivez en face, votre cœur
fait un bond : vous voici nez à nez avec le Seigneur Zahda en
personne ! Il vous toise sans ciller puis, avec un ricanement
mauvais, il pointe sur vous une baguette en platine.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    sommerswerd = has_item("GLAIVE DE SOMMER")
    st.write_stream(stream_text("Si vous possédez le Glaive de Sommer, rendez-vous au :"))
    st.page_link("tomes/tome7/page_174.py", label="174", icon="📄", disabled=not sommerswerd)
    st.write_stream(stream_text("Si vous n'avez pas cet Objet Spécial, rendez-vous au :"))
    st.page_link("tomes/tome7/page_202.py", label="202", icon="📄", disabled=sommerswerd)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
