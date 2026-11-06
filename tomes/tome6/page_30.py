import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
    spend_gold,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=30, book=6)

fr_text = """
Les trois hommes échangent des regards soupçonneux, puis ils
finissent par vous offrir un siège. L'un d'eux, un guerrier au
visage grêlé, fait claquer ses doigts et crie à travers la salle
surpeuplée : « Serveuse, quatre chopes de bière ! » Les
consommations sont servies dans d'énormes bocks en terre cuite qui
doivent facilement contenir chacun un bon litre de bière !
Chancelant sous le poids, la serveuse arrive finalement à
destination et pose les lourdes chopes sur la table. « Cela fera 8
Pièces d'Or, Messire », dit-elle d'une voix essoufflée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous désirez payer la tournée, rendez-vous au 230."))
    if st.button("Payer 8 Couronnes", disabled=st.session_state.purse < 8):
        spend_gold(8)
        st.switch_page("tomes/tome6/page_230.py")

    st.write_stream(stream_text("Si vous ne le souhaitez pas, ou si vous n'en avez pas les moyens, rendez-vous au :"))
    st.page_link("tomes/tome6/page_159.py", label="159", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
