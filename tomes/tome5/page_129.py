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

check_inventory(current_page_number=129, book=5)

fr_text = """
Dissimulé dans l'ombre d'un porche, vous observez le port. La
place est envahie par les soldats de Maouk et il serait vraiment
trop dangereux de vous y risquer. Vous devez trouver un autre
endroit pour vous cacher jusqu'à ce que les quais se vident. Des
groupes de soldats fouillent les maisons qui bordent la place et
vous êtes obligé de quitter votre abri et de remonter l'allée en
courant. Au moment où vous arrivez à nouveau sur la place du
Marché, vous tombez nez à nez avec une douzaine de guerriers
Sharnazims conduits par Maouk en personne.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez les combattre, rendez-vous au :"))
    st.page_link("tomes/tome5/page_36.py", label="36", icon="📄")

    st.write_stream(stream_text("Si vous préférez vous rendre, rendez-vous au :"))
    st.page_link("tomes/tome5/page_176.py", label="176", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
