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

check_inventory(current_page_number=168, book=6)

fr_text = """
Il fait presque nuit lorsque vous apercevez enfin une taverne au
bord de la route. Deux grosses torches crachotent, enfoncées
dans des supports rouillés, éclairant une enseigne accrochée au
dessus de la porte : Auberge du Mi-Chemin. Il s'agit de
l'établissement dont Cyrilus vous avait parlé, et vous regrettez
amèrement qu'il ne soit pas à vos côtés. Alors que vous menez
votre cheval à l'écurie, vous entendez le tonnerre gronder par-
delà les collines. Un bel orage se prépare ! Vous vous rendez
ensuite dans la salle où règne une chaleur réconfortante. La
taverne résonne de conversations animées, de tintements de
chopes qu'on entrechoque et du crépitement du feu qui brûle
dans l'âtre. Au centre de la pièce se dresse une estrade où un
illusionniste accomplit des tours de passe-passe pour le plus
grand plaisir de la clientèle.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez rester à regarder l'illusionniste pendant un moment, rendez-vous au :"))
    st.page_link("tomes/tome6/page_199.py", label="199", icon="📄")

    st.write_stream(stream_text("Si vous préférez aller tout de suite vous occuper de réserver une chambre pour la nuit, rendez-vous au :"))
    st.page_link("tomes/tome6/page_253.py", label="253", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
