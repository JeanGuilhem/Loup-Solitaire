import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    remove_from_inventory,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=24, book=3)

fr_text = """
Vous visez soigneusement et vous lancez le Diamant dans le
couloir. Il rebondit juste devant le Barbare des Glaces et finit sa
course derrière l'escalier. Le Barbare, intrigué par le bruit et par
l'éclat du Diamant, quitte son poste pour aller voir de quoi il
retourne. Vous saisissez cette occasion pour grimper l'escalier
sans vous faire remarquer.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        remove_from_inventory("DIAMANT")
    st.caption("Vous avez lancé le Diamant : il est rayé de vos Objets Spéciaux.")

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome3/page_332.py", label="332", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
