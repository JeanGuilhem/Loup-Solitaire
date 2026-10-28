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

check_inventory(current_page_number=221, book=3)

fr_text = """
Le couloir dans lequel vous vous trouvez maintenant bénéficie
d'une température beaucoup plus clémente que la caverne
glacée. Pour la première fois depuis longtemps, vous pouvez
abaisser le capuchon de votre cape et enlever vos moufles sans
risquer la morsure du gel. Vous remarquez que ce passage monte
vers une sorte de palier où un autre couloir bifurque en direction
de l'est. Des coupes de M'iare sont suspendues à la voûte, à
intervalles réguliers, éclairant d'une lumière insolite les murs
ornés de motifs sculptés. Lorsque vous approchez du palier, vous
apercevez une arcade qui ouvre sur une petite pièce. Vous
découvrez alors un étrange spectacle. Le sol de cette pièce, en
effet, est encombré de fourrures en lambeaux, d'éclats de poterie
et de toutes sortes de débris qui semblent avoir été amassés là
depuis des siècles. Un grand levier est fixé au mur, juste à côté de
l'arcade.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            "Si vous souhaitez entrer dans cette pièce pour examiner les débris qu'elle contient, rendez-vous "
            "au :"
        )
    )
    st.page_link("tomes/tome3/page_38.py", label="38", icon="📄")
    st.write_stream(stream_text("Si vous souhaitez tirer le levier, rendez-vous au :"))
    st.page_link("tomes/tome3/page_163.py", label="163", icon="📄")
    st.write_stream(stream_text("Enfin, si vous préférez poursuivre votre chemin vers l'est, le long du couloir, rendez-vous au :"))
    st.page_link("tomes/tome3/page_237.py", label="237", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
