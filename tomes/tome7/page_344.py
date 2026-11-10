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

check_inventory(current_page_number=344, book=7)

fr_text = """
Votre main heurte quelque chose d'invisible le long du gouffre :
le début d'un pont caché par magie. Vous sentez avec vos doigts
qu'il doit s'agir d'une simple planche, car le passage est mince et
étroit. Les bruits de pas cessent brusquement, vous entendez un
claquement sec comme un coup de fouet et le dos de votre main
se trouve marqué d'une vilaine zébrure rouge. (Vous perdez 2
points d'ENDURANCE.) Vous sentez la présence de celui qui
vous a infligé cette blessure mais vous ne pouvez pas voir votre
ennemi.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-2)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)

    st.write_stream(stream_text("Si vous souhaitez avancer sur le pont invisible, rendez-vous au :"))
    st.page_link("tomes/tome7/page_166.py", label="166", icon="📄")
    st.write_stream(stream_text("Si vous voulez essayer de combattre votre ennemi invisible, rendez-vous au :"))
    st.page_link("tomes/tome7/page_257.py", label="257", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
