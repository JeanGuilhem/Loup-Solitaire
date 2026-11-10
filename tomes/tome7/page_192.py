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

check_inventory(current_page_number=192, book=7)

fr_text = """
Vous reconnaissez les symptômes de la Takadea, appelée
communément « Pourriture des prisons » dans votre pays. Vous
vous approchez de l'homme tremblant et vous le rassurez
aussitôt en lui expliquant que vous ne lui voulez aucun mal et
que, s'il vous fait confiance, vous pourrez sûrement l'aider. Vous
posez vos mains sur ses yeux et vous transmettez à son corps
malade les pouvoirs curatifs de votre Discipline Magnakaï,
concentrant toute votre énergie pour supprimer les terribles
effets de l'infection. Lorsque vous retirez vos mains, ses yeux ne
sont plus opaques et brillent intensément, comme ceux d'un
chat. « Je vois ! s'écrie-t-il, stupéfait, la voix brisée par l'émotion.
Comment pourrais-je jamais vous remercier pour ce miracle. »
Avant que vous ne puissiez lui répondre, vous entendez des
bruits de pas précipités dehors, dans le couloir. « Suivez-moi,
reprend-il en sautant sur ses pieds. Si les gardes de Zahda vous
trouvent ici, ils nous tueront tous les deux ! »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_290.py", label="290", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
