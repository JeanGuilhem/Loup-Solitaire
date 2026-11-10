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

check_inventory(current_page_number=346, book=7)

fr_text = """
Vous sondez désespérément le mur en tapant avec la garde de
votre épée, mais vous n'entendez aucun son creux. Vous perdez
tout espoir de fuite de ce côté mais, au plafond, vous découvrez
une vieille trappe, obstruée par des briques et du mortier, qui
laisse cependant filtrer un mince rayon de lumière scintillante.
Vous tapez violemment sur les briques et, après plusieurs coups,
elles commencent à se fendre et à tomber, ouvrant un large trou
par lequel vous vous glissez. Vous vous retrouvez dans une pièce
où règne une forte odeur d'humus ; vous apercevez au milieu un
énorme sarcophage en granit. Le plafond est soutenu par deux
rangées de gros piliers et deux tunnels, à gauche et à droite,
partent de la pièce. Tout à coup, vous entendez des cliquetis
d'armure et des bruits de pas qui s'approchent dans le passage de
droite.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez vous dissimuler derrière l'un des piliers, rendez-vous au :"))
    st.page_link("tomes/tome7/page_110.py", label="110", icon="📄")
    st.write_stream(stream_text("Si vous voulez quitter cet endroit par le tunnel de gauche, rendez-vous au :"))
    st.page_link("tomes/tome7/page_201.py", label="201", icon="📄")
    st.write_stream(stream_text("Si vous préférez vous tenir en embuscade à l'entrée du tunnel de droite, rendez-vous au :"))
    st.page_link("tomes/tome7/page_319.py", label="319", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
