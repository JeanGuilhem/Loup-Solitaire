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

check_inventory(current_page_number=119, book=7)

fr_text = """
Votre sens Kaï de l'Orientation vous permet de suivre aisément
les traces de Tavig. Tandis que vous rebroussez chemin, de
nombreuses questions vous traversent l'esprit : qu'est-ce qu'un
Trakka ? D'où viennent les Dhax ? Qui est donc ce Zahda que
Tavig semblait craindre tout particulièrement ? Subitement, vous
êtes tiré de vos pensées par un cri provenant du haut d'un
escalier, juste en face de vous. C'est alors que Tavig réapparaît ; il
se tient la tête à deux mains, et du sang coule abondamment
entre ses doigts. Il est sur le point de tomber quand, soudain, une
gigantesque main verte et écailleuse surgit des ténèbres pour s'en
emparer. Le malheureux disparaît en redoublant de cris.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez monter rapidement les marches afin de lui porter secours, rendez-vous au :"))
    st.page_link("tomes/tome7/page_280.py", label="280", icon="📄")

    st.write_stream(stream_text("Si vous préférez prendre la fuite en partant dans la direction opposée, rendez-vous au :"))
    st.page_link("tomes/tome7/page_323.py", label="323", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
