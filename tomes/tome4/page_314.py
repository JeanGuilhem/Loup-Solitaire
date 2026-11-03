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

check_inventory(current_page_number=314, book=4)

fr_text = """
Des groupes de brigands patrouillent dans la forêt, mais sans
manifester de zèle excessif dans l'accomplissement de leur tâche,
et vous parvenez à les éviter sans difficulté. Vous découvrez alors,
par hasard, une petite cabane en rondins cachée au fond des
bois. La flamme d'une chandelle vacille à la fenêtre et la porte est
entrouverte.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez entrer dans la cabane, rendez-vous au :"))
    st.page_link("tomes/tome4/page_53.py", label="53", icon="📄")

    st.write_stream(stream_text("Si vous préférez vous en abstenir, vous poursuivrez votre chemin en vous rendant au :"))
    st.page_link("tomes/tome4/page_258.py", label="258", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
