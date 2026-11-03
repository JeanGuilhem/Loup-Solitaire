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

check_inventory(current_page_number=206, book=4)

fr_text = """
Tandis que les premières lueurs de l'aube éclairent l'horizon,
vous scrutez la grand-route enveloppée de brume en essayant de
repérer le moindre mouvement. Aucun de vos six éclaireurs n'est
encore revenu et les quatre hommes qui vous restent sont aussi
inquiets que vous. Votre marge de manœuvre est limitée: des
hordes de brigands patrouillent en effet au nord ; à l'ouest se
dressent des montagnes hostiles et, à l'est, la ville la plus proche
se trouve à deux jours de cheval.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez pénétrer dans la vallée en suivant la grand-route, rendez-vous au :'))
    st.page_link("tomes/tome4/page_82.py", label="82", icon="📄")

    st.write_stream(stream_text('Si vous préférez descendre dans cette vallée en restant à couvert des arbres de la forêt, rendez-vous au :'))
    st.page_link("tomes/tome4/page_226.py", label="226", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
