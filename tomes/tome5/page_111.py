import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    pickup_button,
    receive_gold,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=111, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
La chaleur et la fatigue du combat vous ont sensiblement affaibli
mais vous venez de vaincre un ennemi si redoutable qu'une
ardeur nouvelle vous remplit le cœur. Vous fouillez le corps de
l'Armurier et vous trouvez 3 Pièces d'Or et une Clé de Cuivre. Si
vous souhaitez garder la Clé, notez-la sur votre feuille d'Aventure
dans la case des Objets Spéciaux.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    receive_gold(3)
    pickup_button("CLÉ DE CUIVRE", key="cle", label="Garder la Clé de Cuivre")

    st.write_stream(stream_text("Si vous souhaitez quitter la forge par la porte nord, rendez-vous au :"))
    st.page_link("tomes/tome5/page_167.py", label="167", icon="📄")

    st.write_stream(stream_text("Si vous préférez quitter les lieux par la porte ouest, rendez-vous au :"))
    st.page_link("tomes/tome5/page_44.py", label="44", icon="📄")

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï de l'Orientation, rendez-vous au :"))
    if has_kai("L'Orientation"):
        st.page_link("tomes/tome5/page_74.py", label="74", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_74.py", label="74", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
