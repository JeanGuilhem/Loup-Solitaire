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

check_inventory(current_page_number=194, book=7)

fr_text = """
Vous essuyez le sang que vous avez sur le visage et sur les mains.
Vous venez d'échapper de justesse à une mort atroce dans les
mâchoires du monstre et, à cette pensée, vous vous sentez pris
d'une nausée que vous avez du mal à réprimer. La lumière
devient soudain plus brillante, et vous entendez retentir au loin
un rire qui vous glace le sang, puis la lumière décroît et revient,
au bout d'un instant, à sa faible intensité initiale. Le rire cesse et
le silence règne à nouveau dans la pénombre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_322.py", label="322", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
