import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=124, book=3)

fr_text = """
Vous sentez une présence de l'autre côté de l'arcade. Vous vous
concentrez de toutes vos forces, mais sans parvenir à deviner s'il
s'agit d'un être animé de bonnes ou de mauvaises intentions.
Vous insistez en déployant toutes les ressources de votre pouvoir
mental, mais rien n'y fait, il vous est impossible d'en savoir
davantage. Votre Discipline Kaï vous a au moins averti que
quelqu'un se trouvait là et vous franchissez donc avec prudence
l'arcade envahie de brume.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome3/page_264.py", label="264", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
