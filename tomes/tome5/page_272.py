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

check_inventory(current_page_number=272, book=5)

fr_text = """
Vous suivez un sentier qui longe le lit, maintenant asséché, d'une
vieille rivière qui jadis coulait à travers les montagnes. Une brise
soulève des tourbillons de poussière rouge le long des rives de
terre aride et stérile. Les bâtisses aux murs blancs d'Ikaresh
apparaissent soudain et, tandis que la poussière retombe
lentement, vous vous retrouvez sur une place près du porche
grand ouvert de la porte est de la ville. Sur un grand monolithe
en basalte, planté au milieu de la place, se trouve un aigle en
bronze, emblème de cette ville de montagne. Dans son bec, le
rapace tient trois flèches indiquant chacune une direction
différente pour sortir de la place.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez aller au nord vers le marché aux Douggas, rendez-vous au :"))
    st.page_link("tomes/tome5/page_376.py", label="376", icon="📄")

    st.write_stream(stream_text("Si vous préférez aller à l'ouest, vers la place principale, rendez-vous au :"))
    st.page_link("tomes/tome5/page_216.py", label="216", icon="📄")

    st.write_stream(stream_text("Si vous souhaitez aller vers le sud en prenant l'avenue des Aigles, rendez-vous au :"))
    st.page_link("tomes/tome5/page_342.py", label="342", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
