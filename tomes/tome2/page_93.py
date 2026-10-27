import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    spend_gold,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=93, book=2)

fr_text = """
Déduisez de votre Feuille d'Aventure le nombre de Pièces d'Or que
vous voulez donner aux mendiants. Ils vous remercient, mais d'autres
mendiants apparaissent aussitôt en demandant que vous leur fassiez
également l'aumône. Finalement, vous parvenez à vous frayer un
chemin dans la foule et vous poursuivez votre route.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    given = st.session_state.get("visibility_alms", False)
    if given is False:
        amount = st.number_input(
            "Nombre de Couronnes à donner aux mendiants",
            min_value=0,
            max_value=st.session_state.purse,
            step=1,
            key="alms_amount",
        )
        if st.button("Donner", key="alms_give") and st.session_state.get("visibility_alms", False) is False:
            spend_gold(int(amount))
            st.session_state["visibility_alms"] = int(amount)
            st.rerun()
    else:
        st.metric(label="Couronnes", value=st.session_state.purse, delta=-given)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_137.py", label="137", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
