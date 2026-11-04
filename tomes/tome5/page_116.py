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

check_inventory(current_page_number=116, book=5)

fr_text = """
Vous gravissez l'escalier en pierre et vous arrivez à une petite
pièce au-dessus du tunnel. L'air y est sec, même si les gaz
pestilentiels de l'égout pénètrent les moindres recoins du
souterrain. Vous suivez un étroit passage qui s'enfonce vers
l'ouest puis tourne brusquement sur la gauche vers le sud. Votre
cœur défaille lorsque vous réalisez que le boyau est sans issue !
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous désirez examiner les lieux afin de trouver une sortie dérobée, rendez-vous au :"))
    st.page_link("tomes/tome5/page_33.py", label="33", icon="📄")

    st.write_stream(stream_text("Si vous préférez retourner sur vos pas et rejoindre le trottoir, rendez-vous au :"))
    st.page_link("tomes/tome5/page_64.py", label="64", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
