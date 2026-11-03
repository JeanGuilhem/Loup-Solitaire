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

check_inventory(current_page_number=223, book=4)

fr_text = """
Vous repoussez la trappe qui donne accès au sommet de la tour
et vous vous hissez au-dehors. Un spectacle navrant s'offre alors
à vos yeux. Des cadavres de soldats du Sommerlund sont en effet
étendus çà et là, leurs armures tordues et fracassées. Tous ont été
cruellement blessés. Un oiseau monstrueux tournoie au-dessus
des cadavres. Ses ailes agitent la fumée répandue dans
l'atmosphère et, de ses serres tranchantes comme des rasoirs, il
déchire et mutile quiconque se trouve à sa portée. Un Guerrier
vêtu d'une armure d'acier est assis à califourchon sur la créature
et brandit un cimeterre taché du sang de vos compatriotes. Il
glisse alors de sa selle incrustée de pierreries et se laisse tomber
au sommet de la tour. Une voix résonne dans votre tête lorsque
le Guerrier s'approche de vous : « Dis tes prières, homme du
Sommerlund, murmure la voix, car ta fin est proche. »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez combattre ce Guerrier, rendez-vous au :'))
    st.page_link("tomes/tome4/page_77.py", label="77", icon="📄")

    st.write_stream(stream_text('Si vous préférez essayer de fuir le combat, rendez-vous au :'))
    st.page_link("tomes/tome4/page_128.py", label="128", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
