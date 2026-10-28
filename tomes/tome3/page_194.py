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

check_inventory(current_page_number=194, book=3)

fr_text = """
Votre habileté et votre patience sont finalement récompensées.
Vous entendez en effet un très léger cliquetis qui vous indique
que vous avez réussi. Vous ôtez alors votre lame de la serrure et
le grand couvercle de pierre se soulève lentement pour laisser
voir un magnifique Casque d'Argent.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez vous coiffer de ce Casque, rendez-vous au :'))
    st.page_link("tomes/tome3/page_308.py", label="308", icon="📄")
    st.write_stream(stream_text("Si vous préférez le laisser au fond de son coffre, vous poursuivrez votre chemin en montant l'escalier ; rendez-vous pour cela au :"))
    st.page_link("tomes/tome3/page_323.py", label="323", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
