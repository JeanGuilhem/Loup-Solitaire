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

check_inventory(current_page_number=193, book=7)

fr_text = """
L'escalier grimpe en tournant à travers la roche dure pendant un
temps qui vous semble infini, mais vous arrivez enfin à un palier
d'où part un tunnel qui s'enfonce dans l'obscurité. Vous vous
apprêtez à entrer lorsque votre instinct Kaï vous signale la
présence d'une marche peu élevée à l'entrée du tunnel. En
regardant de plus près, vous voyez qu'il s'agit d'un carré en
marbre parfait, occupant toute la largeur du tunnel sur trois
mètres.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez éprouver la dalle de marbre avec une arme pour voir si elle ne recèle pas un piège, rendez-vous au :"))
    st.page_link("tomes/tome7/page_183.py", label="183", icon="📄")

    st.write_stream(stream_text("Si vous voulez pénétrer dans le tunnel en sautant par-dessus la dalle, rendez-vous au :"))
    st.page_link("tomes/tome7/page_127.py", label="127", icon="📄")

    st.write_stream(stream_text("Si vous préférez entrer dans le tunnel en marchant franchement sur cette dalle, rendez-vous au :"))
    st.page_link("tomes/tome7/page_277.py", label="277", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
