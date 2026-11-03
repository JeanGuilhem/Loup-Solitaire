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

check_inventory(current_page_number=236, book=4)

fr_text = """
Vous vous approchez des écuries et vous entendez à ce moment
une voix étouffée. Soudain, la porte s'ouvre à la volée pour livrer
passage à deux Guerriers Pillards qui tendent leurs arcs. Des
flèches sifflent aussitôt et des patrouilleurs tombent de leurs
chevaux. Dégainant votre arme, vous vous précipitez sur les
attaquants, mais d'autres brigands surgissent de tous côtés et vos
hommes sont pris sous un feu croisé particulièrement meurtrier.
La rapidité de votre action a cependant semé la panique auprès
des deux archers. Ils font volte-face pour s'enfuir, mais vous les
abattez avant qu'ils aient pu disparaître. Un Guerrier à la peau
sombre, aux cheveux noirs et huileux apparaît alors à une
fenêtre. Il fait un geste de la main et un couteau s'enfonce dans
votre bras. Vous perdez 4 points d'ENDURANCE. Serrant les
dents, vous arrachez le poignard que vous lancez à votre tour en
direction de votre agresseur. L'homme est tué sur le coup. La
main crispée sur votre bras blessé, vous traversez les écuries en
chancelant et vous vous échappez par la porte de derrière.
Devant vous s'étend un terrain escarpé envahi d'une végétation
touffue.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-4)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-4)

    st.write_stream(stream_text('Si vous souhaitez vous enfuir en courant tout droit dans cette forêt, rendez-vous au :'))
    st.page_link("tomes/tome4/page_123.py", label="123", icon="📄")

    st.write_stream(stream_text('Si vous préférez changer de direction dès que vous serez à couvert des arbres, rendez-vous au :'))
    st.page_link("tomes/tome4/page_169.py", label="169", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
