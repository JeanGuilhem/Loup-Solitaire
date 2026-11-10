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

check_inventory(current_page_number=246, book=7)

fr_text = """
Vous avez réussi à faire cesser l'attaque psychique et,
rapidement, vous ne ressentez plus aucune douleur. Cependant,
la vrille caoutchouteuse de la créature continue à se rapprocher
de votre gorge. Vous ramassez votre arme sur le sable noir et
passez à l'attaque. Vous touchez l'extrémité de la vrille mais, au
lieu de sang, ou ce qui devrait passer pour du sang dans le corps
de cette effrayante créature, une flamme jaillit au bout de la vrille
qui s'enflamme comme une mèche. Le cerveau cesse de bouger et
flotte, immobile au-dessus du sable, tandis que le mince filament
de chair continue de brûler.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_170.py", label="170", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
