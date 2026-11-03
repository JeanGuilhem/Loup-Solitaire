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

check_inventory(current_page_number=178, book=4)

fr_text = """
Vous repoussez le cadavre de la répugnante créature pour
dégager le patrouilleur. Hélas ! l'homme est mort. L'Elix lui a
planté ses dents pointues dans le cœur. Empoignant votre arme,
vous vous précipitez aussitôt vers l'autre patrouilleur qui est à
présent attaqué par deux de ces Chats de Guerre géants. Un
troisième Elix bondit sur vous, mais vous lui portez un coup
avant qu'il ait eu le temps de vous atteindre et vous le précipitez
dans le puits.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_245.py", label="245", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
