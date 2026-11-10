import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=42, book=7)

fr_text = """
Le cœur battant, vous tendez la main vers la Pierre de la Sagesse.
Vous tremblez d'excitation à la pensée que, dans un instant, le
grand savoir qu'elle recèle en son sein se transmettra à vous par
son simple contact. Mais au moment d'atteindre ce fabuleux
cristal, une vive douleur vous ramène brutalement à la réalité :
une goutte d'acide sombre et corrosif vient de tomber de la pierre
noire vous transperçant cruellement le dessus de la main (vous
perdez 3 points d'ENDURANCE). Puis une gerbe d'éclairs
aveuglants se met à fuser de toutes parts, entourant la Pierre de
Herdos d'un feu crépitant. Dans la lumière blafarde qui baigne le
trône, vous voyez apparaître le Seigneur Zahda, l'air lugubre et
l'œil sévère. Il tient dans la main une baguette de platine qu'il
pointe soudain vers vous.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-3)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-3)

    glaive = has_item("GLAIVE DE SOMMER")
    st.write_stream(stream_text('Si vous possédez le Glaive de Sommer, rendez-vous au :'))
    st.page_link("tomes/tome7/page_174.py", label="174", icon="📄", disabled=not glaive)

    st.write_stream(stream_text('Si vous ne possédez pas cet Objet Spécial, rendez-vous au :'))
    st.page_link("tomes/tome7/page_202.py", label="202", icon="📄", disabled=glaive)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
