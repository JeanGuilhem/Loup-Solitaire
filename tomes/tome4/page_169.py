import streamlit as st
from combat import combat
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

check_inventory(current_page_number=169, book=4)

fr_text = """
Tandis que vous écartez les feuillages, vous tombez soudain au
bas d'un à-pic dissimulé sous les broussailles. Vous atterrissez
sur un large sentier forestier à moins de 3 mètres d'un brigand
agenouillé qui examine le sabot de son cheval. L'homme est en
train de dégager un éclat de pierre qui s'est glissé sous le fer de
l'animal à l'aide d'un poignard à la lame recourbée. Le bruit de
votre chute le fait sursauter et il se retourne aussitôt en
brandissant son arme. Il vous faut le combattre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("GUERRIER PILLARD", 16, 24)])
    if outcome == "win":
        st.write_stream(stream_text("Vous apercevez un groupe de brigands qui s'approche en provenance du nord. Vous avez alors tout juste le temps de vous enfuir. Rendez-vous au :"))
        st.page_link("tomes/tome4/page_123.py", label="123", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
