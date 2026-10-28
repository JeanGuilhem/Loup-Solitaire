import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    lose_all_weapons,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=196, book=3)

fr_text = """
Votre lutte est désespérée, mais c'est précisément dans ce
désespoir que vous trouvez la force de survivre. Votre arme (ou
vos armes) vous a (ont) été arrachée(s) des mains par le cyclone
et le bombardement de glace et de pierres que vous avez dû subir
vous fait perdre 2 points d'ENDURANCE. Faites les
modifications nécessaires sur votre Feuille d'Aventure. Vous
parvenez cependant à atteindre péniblement l'arcade située au
nord. Vous avez perdu votre (vos) arme(s), mais vous êtes
vivant.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        lose_all_weapons()
        change_endurance(-2)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)
    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome3/page_306.py", label="306", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
