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

check_inventory(current_page_number=338, book=3)

fr_text = """
Vous enjambez les cadavres des Barbares des Glaces et vous
apercevez à ce moment une créature grotesque qui vous observe,
tapie au coin d'un couloir situé à votre gauche. La créature
disparaît aussitôt et vous ne l'avez donc vue que l'espace d'un
bref instant, mais la vision que vous en gardez suffit cependant à
vous faire frissonner d'horreur. Cet être est en effet constitué
d'une énorme tête humaine posée sur de grands pieds et pourvue
d'une longue queue couverte d'écailles. La créature est vêtue
d'une cape à capuchon et, de toute évidence, elle n'a pas de torse.
L'image de cet être de cauchemar vous remplit de dégoût et vous
vous demandez, le cœur battant, quelles autres monstruosités
vous attendent encore.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez vous lancer à la poursuite de l'étrange créature, rendez-vous au :"))
    st.page_link("tomes/tome3/page_87.py", label="87", icon="📄")
    st.write_stream(stream_text("Si vous préférez fouiller les cadavres des Barbares des Glaces, rendez-vous au :"))
    st.page_link("tomes/tome3/page_26.py", label="26", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
