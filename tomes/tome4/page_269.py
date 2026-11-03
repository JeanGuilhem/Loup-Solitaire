import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import called_cookies, handle_repas, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=269, book=4)

fr_text = """
Vous suivez le couloir pendant environ une heure avant d'arriver
devant une paroi rocheuse. Des Pelles et des brouettes ont été
abandonnées sur le sol comme si les hommes qui creusaient ce
souterrain l'avaient fui en toute hâte. Vous pouvez prendre l'une
des Pelles, si vous le souhaitez, mais sachez qu'elle occupera dans
votre Sac à Dos la place de deux objets. Vous avez faim à présent
et il vous faut prendre un Repas, sinon vous perdrez 3 points
d'ENDURANCE. Maudissant votre malchance, vous êtes
contraint de rebrousser chemin jusqu'au croisement.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_button("PELLE", key="pelle", label="Prendre une Pelle")
    handle_repas()
    st.write_stream(stream_text('Vous poursuivez ensuite votre exploration en vous rendant au :'))
    st.page_link("tomes/tome4/page_145.py", label="145", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
