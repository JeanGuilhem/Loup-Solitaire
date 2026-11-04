import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=93, book=5)

fr_text = """
Vous descendez rapidement l'escalier et vous suivez le couloir
menant vers l'est en prenant garde de marcher le plus
silencieusement possible. Les barreaux des hautes fenêtres
projettent un treillage d'ombre sur le marbre lisse du sol. Sous
l'une des fenêtres se trouve une table où est posée une cruche
d'eau. Comme vous avez la gorge desséchée, vous buvez à même
la cruche pour étancher votre soif. Vous gagnez 1 point
d'ENDURANCE.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(1)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=1)
    st.write_stream(stream_text("Si vous désirez à présent grimper sur la table pour regarder par la fenêtre, rendez-vous au :"))
    st.page_link("tomes/tome5/page_155.py", label="155", icon="📄")

    st.write_stream(stream_text("Si vous préférez reprendre votre chemin le long du couloir sans plus tarder, rendez-vous au :"))
    st.page_link("tomes/tome5/page_182.py", label="182", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
