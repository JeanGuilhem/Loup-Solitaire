import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=157, book=2)

fr_text = """
Le GARDE est furieux et il se précipite sur vous en dévalant l'escalier,
son épée levée au-dessus de sa tête. Si vous ne possédez pas d'arme,
réduisez de 4 points votre total d'HABILETÉ et battez-vous à mains nues.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Vous avez le droit de prendre la fuite à tout moment en vous rendant au 65."))
    outcome = combat([("GARDE", 15, 22)], flee_after=0)
    if outcome == "win":
        st.write_stream(stream_text("Si vous êtes vainqueur, rendez-vous au :"))
        st.page_link("tomes/tome2/page_331.py", label="331", icon="📄")
    elif outcome == "fled":
        st.write_stream(stream_text("Vous prenez la fuite. Rendez-vous au :"))
        st.page_link("tomes/tome2/page_65.py", label="65", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
