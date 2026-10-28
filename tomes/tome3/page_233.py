import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=233, book=3)

fr_text = """
Vous reconnaissez ce liquide : c'est une décoction de Laumspur,
une herbe aux propriétés curatives particulièrement efficace.
Cette Potion concentrée permet à celui qui la boit de récupérer 5
points d'ENDURANCE.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez conserver la fiole, inscrivez-la dans vos Objets Spéciaux."))
    if not has_item("POTION ROUGE DE LAUMSPUR"):
        pickup_button("POTION ROUGE DE LAUMSPUR", key="potion_rouge", label="Prendre la fiole de Laumspur")
    st.write_stream(stream_text("Retournez à présent au 10 pour faire un autre choix :"))
    st.page_link("tomes/tome3/page_10.py", label="10", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
