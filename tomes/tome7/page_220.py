import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=220, book=7)

fr_text = """
Votre compagnon retourne le cadavre et retire de la ceinture un
sabre et un poignard. Vous pouvez également prendre la hache
qui a été utilisée au cours du combat si vous le souhaitez. Vous
descendez ensuite les marches et vous vous retrouvez dans un
vestibule fermé par une énorme porte en bronze à double
battant. Des statuettes en or sont alignées de chaque côté, tout le
long du mur recouvert de somptueuses tapisseries, et le
murmure d'une fontaine en marbre sculptée résonne dans le
vestibule. Vous avez à peine parcouru quelques mètres qu'un
garde en armure surgit de derrière la fontaine. Il lève son
arbalète, et vous criez à votre nouveau compagnon de prendre
garde, mais vous l'avez averti trop tard : le carreau fend l'air en
sifflant et le frappe avec une telle force qu'il tombe à la renverse
en heurtant violemment le sol. Le garde sort une nouvelle flèche
de son carquois en cuir et s'apprête à en finir avec vous.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_button("SABRE", key="sabre")
    pickup_button("POIGNARD", key="poignard")
    pickup_button("HACHE", key="hache")

    st.write_stream(stream_text("Si vous souhaitez porter secours à votre compagnon blessé, rendez-vous au :"))
    st.page_link("tomes/tome7/page_28.py", label="28", icon="📄")

    st.write_stream(stream_text("Si vous préférez attaquer le garde avant qu'il n'ait le temps de recharger son arme, rendez-vous au :"))
    st.page_link("tomes/tome7/page_81.py", label="81", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
