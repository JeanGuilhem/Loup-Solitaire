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

check_inventory(current_page_number=358, book=5)

fr_text = """
Vous vous rendez compte que la vieille femme ment en
prétendant être la veuve Soushilla. Elle vous a trompé dans
l'intention de vous escroquer quelques Pièces d'Or. Alors que
vous lui demandez des explications, elle tourne les talons et
disparaît dans l'allée à la vitesse de l'éclair. « Laisse-la, dit
Banedon, notre temps est bien plus précieux que l'or qu'elle nous
a pris. »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez continuer à remonter l'avenue des Aigles, rendez-vous au :"))
    st.page_link("tomes/tome5/page_388.py", label="388", icon="📄")
    st.write_stream(stream_text("Si vous préférez rebrousser chemin vers la place des Aigles, vous pouvez : soit aller vers le nord, en direction du marché aux Douggas, rendez-vous au :"))
    st.page_link("tomes/tome5/page_376.py", label="376", icon="📄")
    st.write_stream(stream_text("soit aller vers l'ouest, en direction de la Grand-Place, rendez-vous alors au :"))
    st.page_link("tomes/tome5/page_216.py", label="216", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
