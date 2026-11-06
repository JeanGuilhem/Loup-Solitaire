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

check_inventory(current_page_number=191, book=6)

fr_text = """
Votre longue chevauchée de la nuit dernière vous a beaucoup
fatigué, mais vous savez que vous devez continuer votre chemin
sans perdre trop de temps si vous voulez être à Soren avant la
tombée de la nuit. Un peu plus loin, la route croise une rivière.
Vous vous accordez une courte halte. Vous vous lavez
rapidement et vous reposez un peu. Vous devez aussi prendre un
Repas ou bien perdre 3 points d'ENDURANCE. Vous passez
ensuite la rivière à gué et apercevez, de l'autre côté, un poteau
indicateur tourné vers l'ouest : Soren 40 kilomètres.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    handle_repas()

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_102.py", label="102", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
