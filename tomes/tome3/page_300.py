import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=300, book=3)

fr_text = """
Pendant trois jours et trois nuits vous parcourez les étendues
mornes et hostiles du glacier de Viad. Irian et Fenor ont tous
deux souffert de cécité des neiges et il semble que le vent
implacable qui souffle du nord épuise les forces de chacun. Au
matin du quatrième jour, le vent tombe enfin et vous pouvez
faire le point pour calculer votre position exacte. A la
consternation générale, Irian annonce alors que vous vous êtes
sensiblement écartés de votre route. Face à vous, les crêtes grises
d'une chaîne de montagnes se dessinent dans les neiges du nord,
offrant un spectacle sinistre et menaçant. «Ce sont les monts
Myjavik, constate Dyce, nous sommes allés trop loin à l'est. » Son
visage barbu exprime une amère déception. Les monts Myjavik
se dressent à présent entre la forteresse et vous. Pour les
franchir, vous devrez abandonner chiens et traîneaux, porter
votre matériel sur le dos et poursuivre votre chemin à pied. Il y a
une autre possibilité, mais elle vous ferait perdre deux jours qui
pourraient être précieux : il s'agirait de revenir en arrière
jusqu'au glacier pour reprendre là votre route jusqu'à Ikaya.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez abandonner les traîneaux et les chiens pour franchir à pied les monts Myjavik, rendez-vous au :'))
    st.page_link("tomes/tome3/page_12.py", label="12", icon="📄")

    st.write_stream(stream_text('Si vous préférez perdre deux jours et revenir sur le glacier de Viad, rendez-vous au :'))
    st.page_link("tomes/tome3/page_238.py", label="238", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
