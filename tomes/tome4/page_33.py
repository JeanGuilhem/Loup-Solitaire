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

check_inventory(current_page_number=33, book=4)

fr_text = """
La nuit est presque tombée lorsque vous atteignez une vallée
envahie d'une forêt touffue. La grand-route disparaît au loin
parmi les arbres et vous apercevez un panneau indicateur
montrant la direction du sud. Vous n'êtes plus à présent qu'à 60
km de Ruanon, mais vos hommes sont fatigués et ont besoin de
manger et de se reposer.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez établir votre campement en lisière de la forêt, rendez-vous au :"))
    st.page_link("tomes/tome4/page_74.py", label="74", icon="📄")

    st.write_stream(stream_text("Si vous préférez envoyer des éclaireurs dans la vallée pour repérer d'éventuels brigands, rendez-vous au :"))
    st.page_link("tomes/tome4/page_139.py", label="139", icon="📄")

    st.write_stream(stream_text("Enfin, si vous décidez de poursuivre votre chemin vers Ruanon sans manger ni dormir, rendez-vous au :"))
    st.page_link("tomes/tome4/page_251.py", label="251", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
