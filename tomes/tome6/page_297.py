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

check_inventory(current_page_number=297, book=6)

fr_text = """
Le cours de la bataille tourne en votre faveur. Les pirates
pensaient s'emparer facilement d'un joli butin, mais votre
furieuse résistance les a complètement découragés, et ils
s'enfuient de toutes parts en essayant tant bien que mal de
rejoindre leurs chaloupes. Le Capitaine poursuit impitoyablement
les fuyards, puis il se fraye un chemin vers le bastingage que le
chef des pirates s'apprête à enjamber. Il le saisit par le collet
et le traîne jusqu'au grand mât. Il lui cogne la tête, une, deux,
trois fois avec une telle rage, que le bois commence à se
fendiller, puis il le relâche sur le pont, le crâne fracassé sous
son casque de cuir. La bataille s'achève aussi brusquement qu'elle
avait commencé, et les rares pirates qui ont survécu disparaissent
happés par le brouillard. On déplore peu de pertes dans les rangs
des mercenaires, mais l'équipage du bateau a été massacré. Les
pirates l'avaient enfermé dans la cale au début du combat et un
seul homme a pu échapper à leurs lames mortelles. Le Capitaine
prend le commandement du navire. Il dirige les réparations et
surveille les funérailles. Tandis que les corps s'enfoncent dans
les eaux noires de la rivière, le Kazonara émerge lentement du
brouillard, et vous apercevez au loin les accueillants rivages de
Luyen.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_19.py", label="19", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
