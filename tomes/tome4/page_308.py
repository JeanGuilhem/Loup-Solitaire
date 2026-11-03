import streamlit as st
from combat import combat
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

check_inventory(current_page_number=308, book=4)

fr_text = """
Vous tournez la clé dans la serrure et vous poussez la porte de
fer. Aussitôt, un sifflement sonore retentit comme un jet de
vapeur s'échappant d'un geyser. Une créature aux allures de chat
surgit alors de l'obscurité et bondit sur vous en vous projetant
à terre. Les yeux de l'animal brillent d'une lueur verte et son
haleine fétide vous brûle le visage : c'est un Elix ! Tandis que
vous essayez de repousser la créature à la gueule hérissée de
dents pointues, plusieurs autres de ses congénères sautent sur
vos hommes. Vous ne pouvez pas prendre la fuite et il vous faut
combattre l'animal jusqu'à la mort de l'un de vous deux.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("ÉLIX", 17, 30)])
    if outcome == "win":
        st.write_stream(stream_text("Si vous remportez la victoire, rendez-vous au :"))
        st.page_link("tomes/tome4/page_127.py", label="127", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
