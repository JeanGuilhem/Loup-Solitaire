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

check_inventory(current_page_number=279, book=5)

fr_text = """
Un étroit couloir s'ouvre devant vous, éclairé par la lumière
orangée du soleil couchant qui pénètre dans les lieux par de
petites fenêtres ouvertes situées en haut des parois ornementées.
L'air résonne de bruits de pas hâtifs, car le grand Palais est en
alerte générale. Les Gardes du Palais et les sauvages Drakkars
sont tous à votre recherche et ils sont bien déterminés à vous
trouver puis à vous tuer, car leur propre vie sera menacée en cas
d'échec. Vous arrivez à une porte qui s'ouvre sur un balcon
extérieur. Des marches descendent vers un pont qui relie le
Palais principal à une haute tour de marbre blanc. L'escalier lui-même
continue au-delà du pont, puis disparaît vers les jardins
du Palais situés en contrebas. Vous n'apercevez aucun soldat sur
le pont ni dans les jardins.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez descendre sur le pont puis entrer dans la tour de marbre, rendez-vous au :"))
    st.page_link("tomes/tome5/page_396.py", label="396", icon="📄")

    st.write_stream(stream_text("Si vous souhaitez passer le pont puis descendre l'escalier vers les jardins du Palais, rendez-vous au :"))
    st.page_link("tomes/tome5/page_215.py", label="215", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
