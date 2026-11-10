import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    has_magnakai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=90, book=7)

fr_text = """
Tandis que vous progressez, la température ambiante augmente
progressivement jusqu'à ce que vous soyez trempé de sueur. Les
plaques d'acier irradient une chaleur intense, et des volutes de
fumée s'élèvent de la semelle de vos bottes ; celles-ci semblent
sur le point de fondre tant le sol est brûlant !
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    protected = has_magnakai("Nexus") or has_item("AMULETTE EN PLATINE")
    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de Nexus, ou si vous possédez une Amulette en Platine, rendez-vous au :"))
    st.page_link("tomes/tome7/page_24.py", label="24", icon="📄", disabled=not protected)
    st.write_stream(stream_text("Si vous ne possédez ni cette Discipline ni l'Objet Spécial en question, rendez-vous au :"))
    st.page_link("tomes/tome7/page_324.py", label="324", icon="📄", disabled=protected)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
