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

check_inventory(current_page_number=217, book=7)

fr_text = """
Grâce à votre Discipline Magnakaï, vous parvenez à faire cesser
la douleur qui vous déchire le cerveau et vous recouvrez
rapidement tous vos moyens. Après avoir ramassé votre arme sur
le sable noir et brûlant, vous passez à l'attaque. Vous blessez
l'extrémité de la vrille mais cette dernière, au lieu de perdre du
sang, ou ce qui devrait passer pour du sang dans le corps d'une
créature si épouvantable, s'enflamme comme une mèche. Le
cerveau cesse de bouger, flottant, immobile, au-dessus du sable
tandis que son mince filament de chair se consume rapidement.
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
