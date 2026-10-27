import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    remove_from_inventory,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=141, book=2)

fr_text = """
Le mât s'écrase sur le pont et un débris de bois vous frappe à la tête en
vous jetant par-dessus bord. Vous vous débattez dans les vagues pour
refaire surface puis vous vous agrippez à un panneau d'écoutille qui
flotte à portée de main. A moitié assommé, vous perdez 2 points
d'ENDURANCE. Vous vous hissez ensuite sur ce radeau de fortune en
vous y cramponnant de toutes vos forces : si vous portez une cotte de
mailles, il faut vous en débarrasser immédiatement, sinon, vous êtes sûr
de périr noyé. Rayez-la de votre Feuille d'Aventure. Vous êtes soudain
pris de vertige, vous vous sentez mal, et tandis que la forte houle vous
ballotte en tous sens, vous sombrez peu à peu dans l'inconscience.
Lorsque vous vous réveillez au bout de plusieurs heures, la tempête
s'est calmée. A en juger par la position du soleil, l'après-midi touche à
sa fin. Au loin, vous apercevez un petit bateau de pêche et au-delà, un
rivage qui se dessine à l'horizon. Il ne reste plus du Sceptre Vert que le
panneau d'écoutille sur lequel vous êtes assis.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-2)
        remove_from_inventory("COTTE DE MAILLES")
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)
    st.write_stream(stream_text("Si vous voulez essayer de signaler votre présence au bateau de pêche en agitant votre cape, rendez-vous au :"))
    st.page_link("tomes/tome2/page_278.py", label="278", icon="📄")
    st.write_stream(stream_text("Si vous préférez ne pas vous occuper du bateau et tenter de rejoindre la côte en pagayant à l'aide de vos seules mains, rendez-vous au :"))
    st.page_link("tomes/tome2/page_337.py", label="337", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
