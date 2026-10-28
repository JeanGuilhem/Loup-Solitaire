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

check_inventory(current_page_number=42, book=3)

fr_text = """
Vous tirez le Glaive magnifique de son fourreau et vous en
frappez la porte à coups redoublés. A chaque fois que le Glaive de
Sommer ébrèche l'antique pierre, une gerbe d'étincelles illumine
la pièce. La lame de l'épée rayonne d'un intense flamboiement
d'or tandis que vous l'abattez avec force. Le Glaive de Sommer
parviendra sans nul doute à détruire la pierre, mais il vous
faudra plusieurs heures pour pratiquer une ouverture qui vous
permette de vous enfuir.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            "Si vous souhaitez continuer à marteler la porte à l'aide du Glaive de Sommer, "
            'rendez-vous au :'
        )
    )
    st.page_link("tomes/tome3/page_294.py", label="294", icon="📄")

    st.write_stream(
        stream_text(
            'Si vous préférez abandonner, vous pouvez quitter la pièce par le passage secret aménagé '
            'dans le mur nord ; rendez-vous pour cela au :'
        )
    )
    st.page_link("tomes/tome3/page_145.py", label="145", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
