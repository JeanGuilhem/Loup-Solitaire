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

check_inventory(current_page_number=209, book=5)

fr_text = """
Au moment où vous atteignez le palier, vous voyez trois Drakkars
pénétrer dans la tour. Tandis qu'ils commencent à gravir les
marches, des rires maniaques et lugubres s'élèvent des masques
à tête de mort qui recouvrent leur visage. Bientôt, d'autres
guerriers Drakkars arrivent en grand nombre sur le pont pour
leur prêter main-forte. Quelques-uns possèdent des arbalètes et
vous vous rendez compte qu'il serait suicidaire de passer à
l'attaque. Sans perdre un instant, vous continuez à grimper les
marches quatre à quatre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_322.py", label="322", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
