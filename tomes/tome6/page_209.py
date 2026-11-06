import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
    use_arrow,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=209, book=6)

fr_text = """
Tout tremblant de peur, vous tendez la corde de votre Arc et
décochez votre flèche. Mais la pointe renforcée se détache de la
flèche qui va s'écraser contre le mur de la crypte. Vous n'avez pas
le temps de tirer une seconde fois. Vous abandonnez l'Arc et vous
préparez à un affrontement à mains nues avec la créature qui
avance sur vous.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # la flèche est perdue ; l'Arc est posé pour le combat, le texte ne dit pas qu'il est perdu
    if is_new_page():
        use_arrow()
    st.write(f"*Vous rayez une flèche : il vous en reste {st.session_state.get('arrows', 0)}.*")

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_344.py", label="344", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
