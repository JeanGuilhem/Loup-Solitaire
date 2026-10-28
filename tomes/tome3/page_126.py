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

check_inventory(current_page_number=126, book=3)

fr_text = """
Vous remarquez que les murs et le plafond du couloir sont
couverts d'étranges sculptures. Elles semblent représenter de
petits cyclones ou des tornades qui changent peu à peu de forme
pour prendre une apparence presque humaine. Bien que ces
hiéroglyphes vous intriguent, vous ne vous attardez pas à les
examiner et vous poursuivez votre chemin. Un peu plus loin, le
tunnel tourne brusquement vers la droite. Vous apercevez alors
une autre porte de pierre aménagée dans le mur nord. Le levier
qui la commande est relevé et la porte fermée. Au bout du
couloir, après la porte, un escalier monte vers de mystérieuses
ténèbres.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez examiner cette porte, rendez-vous au :"))
    st.page_link("tomes/tome3/page_246.py", label="246", icon="📄")
    st.write_stream(stream_text("Si vous préférez continuer tout droit et monter l'escalier, rendez-vous au :"))
    st.page_link("tomes/tome3/page_323.py", label="323", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
