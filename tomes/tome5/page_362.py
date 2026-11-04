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

check_inventory(current_page_number=362, book=5)

fr_text = """
La fumée de la pipe est fraîche et parfumée. Malheureusement
on ne peut pas en dire autant de vos hôtes ! Leurs longs
manteaux en peau de Douggas dégagent une odeur musquée qui
ne flatte guère les narines délicates d'un Sommerlundois. Une
jeune fille apparaît en portant sur un plateau des tasses fumantes
emplies de Jala. « Une Pièce d'Or la tasse », dit-elle en posant
son plateau sur la table.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez vous offrir une tasse de ce délicieux breuvage, payez 1 Pièce d'Or, puis rendez-vous au :"))
    if st.button("Payer 1 Couronne", disabled=st.session_state.purse < 1):
        spend_gold(1)
        st.switch_page("tomes/tome5/page_237.py")
    st.write_stream(stream_text("Si vous n'en avez pas les moyens, ou si vous ne voulez pas acheter une tasse de Jala, prenez congé de vos hôtes et quittez l'auberge, puis rendez-vous au :"))
    st.page_link("tomes/tome5/page_388.py", label="388", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
