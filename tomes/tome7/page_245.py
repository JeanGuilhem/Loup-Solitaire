import streamlit as st
from combat import combat
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

check_inventory(current_page_number=245, book=7)

fr_text = """
Le loup se rapproche rapidement en bondissant et vous saute à la
gorge. Entraîné par son énorme poids, vous tombez violemment
à la renverse. Vous voyez ses crocs qui brillent devant vos yeux,
et une salive brûlante vous pique la peau. Vous luttez
désespérément de toutes vos forces pour votre survie. La
créature est immunisée contre la Puissance Psychique mais pas
contre le Foudroiement Psychique.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("LOUP DE LA MORT", 22, 40)], psychic_power_immune=True)
    if outcome == "win":
        st.write_stream(stream_text("Si vous remportez le combat, rendez-vous au :"))
        st.page_link("tomes/tome7/page_259.py", label="259", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
