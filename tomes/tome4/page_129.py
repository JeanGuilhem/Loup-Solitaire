import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, handle_repas, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=129, book=4)

fr_text = """
Vous arrivez bientôt à un endroit du tunnel où le sol s'est
effondré. Une profonde crevasse s'est formée que l'on peut
traverser grâce à une passerelle de fortune. Cette passerelle elle-même
est trouée en plusieurs endroits, mais vous parvenez
malgré tout à la franchir. Vous avez faim à présent et il vous faut
prendre un Repas, sinon vous perdrez 3 points d'ENDURANCE.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    handle_repas()

    st.write_stream(stream_text("Faites les modifications nécessaires sur votre Feuille d'Aventure, puis rendez-vous au :"))
    st.page_link("tomes/tome4/page_309.py", label="309", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
