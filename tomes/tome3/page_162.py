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

check_inventory(current_page_number=162, book=3)

fr_text = """
Le traîneau est déchargé et le matériel qu'il contenait transporté
de l'autre côté de la gorge à raison d'un objet par voyage. Tout se
passe comme prévu, et il ne reste plus qu'à franchir une dernière
fois le pont avec le traîneau lui-même. C'est Dyce qui le conduit
en le maintenant à grand-peine au milieu du pont étroit. Mais
soudain les deux chiens de tête glissent et tombent dans la gorge.
Ils restent suspendus par leur harnais et poussent de longs
gémissements en se débattant inutilement dans le vide. Dyce tire
frénétiquement sur les rênes pour essayer d'empêcher les autres
chiens de tomber à leur tour, mais ses efforts restent vains : un
par un, en effet, les quatre autres chiens de l'attelage sont attirés
dans le précipice par le poids grandissant de ceux qui sont déjà
tombés. « Saute, Dyce, saute ! » hurle Irian tandis que le dernier
chien disparaît dans le vide. Dyce bondit juste à temps, avant que
le traîneau ne bascule dans la gorge, mais il atterrit à l'endroit où
le pont est le plus étroit et perd l'équilibre. Dans un geste
désespéré, il parvient à s'agripper au rebord de glace, mais ses
mains glissent inexorablement. « Au secours ! Aidez-moi ! »
s'écrie-t-il.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez essayer de sauver Dyce, rendez-vous au :'))
    st.page_link("tomes/tome3/page_19.py", label="19", icon="📄")
    st.write_stream(stream_text("Si vous pensez qu'il n'y a aucun moyen de lui venir en aide, rendez-vous au :"))
    st.page_link("tomes/tome3/page_257.py", label="257", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
