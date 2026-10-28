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

check_inventory(current_page_number=7, book=3)

fr_text = """
Soudain, le bloc noir explose en centaines d'éclats de pierre
tranchants comme des rasoirs. Vous avez le dos quelque peu
écorché, et les oreilles vous tintent mais, en dehors de ces menus
désagréments, vous êtes indemne. En vous réfugiant dans le coin
de la salle, vous avez échappé à des blessures qui auraient pu être
graves. Il est clair à présent que le monolithe avait pour fonction
d'interdire l'entrée aux intrus ou de les prendre au piège. Un
ancien mage l'avait sans doute doté de pouvoirs de protection.
Tandis que la poussière noire retombe lentement, vous
remarquez qu'un panneau s'est ouvert dans le mur du nord,
révélant un obscur passage qui permet de quitter la salle.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez essayer de sortir par là, rendez-vous au :'))
    st.page_link("tomes/tome3/page_145.py", label="145", icon="📄")

    st.write_stream(
        stream_text(
            "Si vous préférez essayer d'ouvrir à nouveau la porte par laquelle vous êtes entré, "
            'rendez-vous au :'
        )
    )
    st.page_link("tomes/tome3/page_242.py", label="242", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
