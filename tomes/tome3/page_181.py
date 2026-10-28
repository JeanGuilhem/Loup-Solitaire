import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=181, book=3)

fr_text = """
Les Pièces d'Or tombent sur le sol dans un tintement, mais elles
ne produisent pas l'effet escompté. Le Barbare des Glaces, en
effet, reste à son poste sans prêter la moindre attention aux
Pièces d'Or qui se trouvent à quelques mètres de lui.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez faire une nouvelle tentative en lançant d'autres Pièces d'Or, retournez au :"))
    if st.session_state.purse > 0:
        st.page_link("tomes/tome3/page_152.py", label="152", icon="📄")
    else:
        st.write_stream(stream_text("Vous n'avez plus de Pièces d'Or."))
        st.page_link("tomes/tome3/page_152.py", label="152", icon="📄", disabled=True)
    st.write_stream(stream_text("Si vous n'avez plus de Pièces d'Or, ou si vous ne voulez pas recommencer, vous pouvez attaquer le garde en vous rendant au :"))
    st.page_link("tomes/tome3/page_208.py", label="208", icon="📄")
    st.write_stream(stream_text("Enfin, si vous préférez revenir sur vos pas le long du couloir, retourner au croisement et emprunter le tunnel orienté à l'ouest, rendez-vous au :"))
    st.page_link("tomes/tome3/page_189.py", label="189", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
