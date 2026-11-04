import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=183, book=5)

fr_text = """
La tête du guerrier émerge tout à coup de la bouche d'égout. Il s'attaque violemment à votre jambe, vous tailladant
méchamment le mollet. Vous perdez 2 points d'ENDURANCE.
Fou de colère et de douleur, vous levez la jambe et, de toutes vos
forces, vous décochez au Garde un coup de pied en pleine figure.
Il pousse un cri et tombe en arrière dans l'égout avec un plouf
sonore et sinistre. Vous replacez la dalle de pierre puis vous tirez
une lourde barre que vous placez en travers avant de reprendre
votre chemin à travers le dédale des rues de la ville. Puisque vous
n'avez plus aucune chance de pouvoir signer le traité de paix avec
le nouveau Zakhan, vous n'avez plus rien à faire à Barrakeesh et
vous devez maintenant trouver un moyen quelconque pour
rentrer au Sommerlund le plus vite possible.
Finalement, vous arrivez à une place animée où se tient un
marché. Votre regard est attiré par une enseigne accrochée au-
dessus de l'entrée d'une grande bâtisse : BAINS PUBLICS DE
BARRAKEESH. A ce moment, l'odeur de vos vêtements vous
rend passablement malade. Vous ouvrez la porte sans hésitation
et vous vous glissez à l'intérieur.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-2)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome5/page_90.py", label="90", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
