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

check_inventory(current_page_number=98, book=5)

fr_text = """
Le léger frottement de pas furtifs vous avertit que vous n'êtes pas
seul. Vous vous retournez vivement et vous vous ramassez sur
vous-même, en position de combat. Ce réflexe vous permet
d'éviter une fléchette empoisonnée que quelqu'un vient de lancer
avec une sarbacane. La pointe vient se planter dans la capuche de
votre manteau et vous apercevez votre adversaire en train de
prendre une autre fléchette à sa ceinture. Derrière lui se tiennent
deux guerriers, armés chacun d'un trident acéré. Les trois
hommes bloquent le passage et vous ne pouvez pas fuir.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous désirez passer à l'attaque avant que l'homme à la sarbacane n'ait le temps de recharger son arme, rendez-vous au :"))
    st.page_link("tomes/tome5/page_168.py", label="168", icon="📄")

    st.write_stream(stream_text("Si vous préférez attendre, sans vous battre, et essayer d'esquiver à nouveau la seconde fléchette, rendez-vous au :"))
    st.page_link("tomes/tome5/page_118.py", label="118", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
