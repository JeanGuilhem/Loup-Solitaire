import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=267, book=2)

fr_text = """
Lorsque vous refaites surface, vous constatez que la bataille fait rage
tout autour de vous. Nombre de cadavres de soldats tués au combat ou
jetés par-dessus bord et noyés flottent sur la mer. Vous parcourez à la
nage une trentaine de mètres environ, puis vous vous hissez sur le pont
d'un navire de la flotte de Durenor. Une rude bataille s'y livre car un
vaisseau fantôme vient de l'aborder et d'y déverser une armée de
Zombies qui massacrent à tour de bras les soldats durenorais frappés de
terreur.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous estimez opportun de dégainer le Glaive de Sommer et de vous lancer à l'attaque, rendez-vous au :"))
    st.page_link("tomes/tome2/page_128.py", label="128", icon="📄")

    st.write_stream(stream_text('Si vous préférez sauter sur le pont du vaisseau fantôme, rendez-vous au :'))
    st.page_link("tomes/tome2/page_309.py", label="309", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
