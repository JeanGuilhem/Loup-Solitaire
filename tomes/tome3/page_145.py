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

check_inventory(current_page_number=145, book=3)

fr_text = """
Ce couloir n'est pas très long et vous arrivez bientôt dans une
autre salle aux murs de pierre. Un peu plus loin un escalier mène
à une arcade plongée dans l'ombre, à bonne distance au-dessus
du sol. Au pied de cet escalier, vous distinguez le squelette d'un
ancien gardien de tombes, encore vêtu de son armure et toujours
debout. Ses phalanges nues tiennent une grande épée noire.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez monter l'escalier sans prêter attention au squelette, rendez-vous au :"))
    st.page_link("tomes/tome3/page_36.py", label="36", icon="📄")
    st.write_stream(stream_text("Si vous préférez attaquer le squelette, rendez-vous au :"))
    st.page_link("tomes/tome3/page_278.py", label="278", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
