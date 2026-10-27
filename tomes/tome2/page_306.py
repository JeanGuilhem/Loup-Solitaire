import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=306, book=2)

fr_text = """
Le soldat vous donne un coup de lance en visant votre poitrine, mais
vous faites un pas de côté et le fer vous écorche à peine le bras. Le
GARDE est décidé à se battre ; or, vous ne voulez pas le tuer,
simplement essayer de l'assommer. Menez ce combat à la manière
habituelle, mais en multipliant par 2 les points d'ENDURANCE perdus
par votre adversaire. Lorsque son total d'ENDURANCE sera descendu
à zéro, vous aurez réussi à le mettre hors de combat. En ce qui vous
concerne, tous les points d'ENDURANCE que vous perdrez lors de cet
affrontement seront normalement déduits de votre total.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.caption(
        "Les points d'ENDURANCE perdus par le garde comptent double : son total de 24 est ramené à 12, "
        "ce qui revient au même."
    )
    outcome = combat([("GARDE FRONTALIER", 16, 12)])
    if outcome == "win":
        st.write_stream(stream_text("Si vous parvenez à assommer ce soldat, rendez-vous au :"))
        st.page_link("tomes/tome2/page_35.py", label="35", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
