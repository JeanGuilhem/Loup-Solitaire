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

check_inventory(current_page_number=253, book=7)

fr_text = """
Vous visez rapidement et tirez, mais votre flèche ne fait
qu'égratigner le front de la créature qui se précipite sur le pont
en hurlant de fureur. Elle se jette sur vous en essayant de vous
griffer et de vous mordre au visage, mais vous lâchez votre arc et
vous tirez une arme juste à temps pour contrer son attaque.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Vous pouvez fuir le combat à tout moment en courant vers l'entrée de l'autre tunnel."))
    outcome = combat([("DHAX", 20, 26)], flee_after=0)
    if outcome == "fled":
        st.write_stream(stream_text("Vous fuyez vers l'entrée de l'autre tunnel : rendez-vous au :"))
        st.page_link("tomes/tome7/page_277.py", label="277", icon="📄")
    elif outcome == "win":
        st.write_stream(stream_text("Si vous remportez le combat, rendez-vous au :"))
        st.page_link("tomes/tome7/page_141.py", label="141", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
