import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, handle_repas, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=126, book=4)

fr_text = """
L'obscurité de la nuit descend bientôt sur la Voie de Ruanon et
vous êtes contraints de vous arrêter pour établir votre
campement. Vos hommes allument un grand feu et des
sentinelles montent la garde pour prévenir toute attaque-surprise
au cours de la nuit. Il vous faut à présent prendre un
Repas, sinon vous perdrez trois points d'ENDURANCE. La nuit
se passe sans incident et vous levez le camp à l'aube en
poursuivant votre chemin à travers la Contrée des Pillards.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    handle_repas()

    st.write_stream(stream_text('Utilisez la Table de Hasard pour obtenir un chiffre.'))
    roll = hazard_roll()
    if roll is not None and roll <= 4:
        st.write_stream(stream_text('Si vous tirez un chiffre entre 0 et 4, rendez-vous au :'))
        st.page_link("tomes/tome4/page_25.py", label="25", icon="📄")
    elif roll is not None:
        st.write_stream(stream_text('Entre 5 et 9, rendez-vous au :'))
        st.page_link("tomes/tome4/page_171.py", label="171", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
