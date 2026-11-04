import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=288, book=5)

fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
Le Drakkar vous maudit en exhalant son dernier souffle, puis il
tombe de la plate-forme, son douloureux cri d'agonie se perdant
dans l'espace. Vous vous précipitez pour aider votre compatriote
blessé, mais la bataille n'est pas encore terminée. Un cavalier sur
sa monture Kraan fond sur vous, une arbalète pointée vers votre
tête. Il vous décoche un carreau qui file droit vers votre visage
mais, tout à coup, un bruit aigu et métallique résonne à vos
oreilles, tandis que la flèche rebondit au loin comme par miracle
après avoir ricoché sur un bouclier invisible.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez le Pendentif à l'Étoile de Cristal, rendez-vous au :"))
    if has_item("PENDENTIF À L'ÉTOILE DE CRISTAL"):
        st.page_link("tomes/tome5/page_399.py", label="399", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome5/page_399.py", label="399", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous ne possédez pas cet Objet Spécial, rendez-vous au :"))
    if has_item("PENDENTIF À L'ÉTOILE DE CRISTAL"):
        st.page_link("tomes/tome5/page_294.py", label="294", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome5/page_294.py", label="294", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
