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

check_inventory(current_page_number=110, book=7)

fr_text = """
Quatre guerriers à l'air féroce avancent de front dans le vestibule.
De prime abord, vous pensez, en voyant leur armure noire et leur
casque en forme de tête de mort, que ce sont des Drakkarims - de
malfaisants guerriers à la solde des Seigneurs des Ténèbres
d'Helgedad. Pourtant, lorsqu'ils font halte devant le sarcophage,
vous réalisez qu'il ne peut en aucun cas s'agir d'êtres humains.
De leurs épaules tombantes partent des bras anormalement
longs, prolongés par de grosses mains couvertes de poils roux et
munies d'ongles jaunâtres et recourbés. Ils traînent derrière eux
une longue queue noire, au bout touffu comme celle des lions.
Après quelques instants, le chef grogne un ordre et s'approche de
la grande tombe en granit gris. Il lève son poing velu, appuie sur
trois boutons incrustés dans la pierre tombale ; aussitôt, un
panneau secret s'ouvre en coulissant silencieusement, et tous
quatre disparaissent alors de votre vue. Le panneau se referme
immédiatement sur eux.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez examiner le sarcophage, rendez-vous au :"))
    st.page_link("tomes/tome7/page_83.py", label="83", icon="📄")

    st.write_stream(stream_text("Si vous préférez quitter le vestibule par le tunnel où sont apparus les guerriers, rendez-vous au :"))
    st.page_link("tomes/tome7/page_323.py", label="323", icon="📄")

    st.write_stream(stream_text("Si vous jugez plus prudent d'emprunter le tunnel de gauche, rendez-vous au :"))
    st.page_link("tomes/tome7/page_201.py", label="201", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
