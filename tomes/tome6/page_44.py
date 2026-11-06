import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=44, book=6)

fr_text = """
Soudain, il se produit une terrible secousse, et vous vous trouvez
projeté la tête la première contre le bastingage. (Vous perdez 2
points d'ENDURANCE.) Le crissement aigu du métal tordu et le
craquement sec du bois fracassé déchirent le silence au moment où
le Kazonara, fortement ébranlé par le choc, tangue et pique
profondément du nez dans les eaux de la rivière. Le bateau vient
de heurter un barrage flottant constitué par des troncs d'arbres
reliés les uns aux autres par de grosses chaînes.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-2)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_224.py", label="224", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
