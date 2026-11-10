import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    pickup_gold,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=80, book=7)

fr_text = """
En dépit de l'alarme qui carillonne et du martèlement de bottes
qui se rapproche, vous prenez le temps de fouiller rapidement le
corps de vos ennemis avant de vous engouffrer dans l'escalier.
Voici ce que vous trouvez sur eux :
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.markdown("- 1 Lance\n- 2 Sabres\n- 1 Hache\n- 2 Poignards\n- 1 Masse d'armes\n- 6 Pièces d'Or")
    pickup_button("LANCE", key="lance", label="Prendre la Lance")
    pickup_button("SABRE", key="sabre_1", label="Prendre un Sabre")
    pickup_button("SABRE", key="sabre_2", label="Prendre le second Sabre")
    pickup_button("HACHE", key="hache", label="Prendre la Hache")
    pickup_button("POIGNARD", key="poignard_1", label="Prendre un Poignard")
    pickup_button("POIGNARD", key="poignard_2", label="Prendre le second Poignard")
    pickup_button("MASSE D'ARMES", key="masse", label="Prendre la Masse d'armes")
    pickup_gold(6, key="or_80")

    st.write_stream(stream_text("Si vous souhaitez conserver certains de ces Objets, n'oubliez pas de faire les modifications nécessaires sur votre Feuille d'Aventure. Ensuite, rendez-vous au :"))
    st.page_link("tomes/tome7/page_55.py", label="55", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
