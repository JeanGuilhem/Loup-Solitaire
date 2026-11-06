import streamlit as st
from inventory import (
    check_inventory,
    clear_flag,
    display_inventory,
    end_page,
    is_new_page,
    receive_gold,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=62, book=6)

fr_text = """
Vous avez raison : le garçon a les cheveux blonds et la fille
les cheveux noirs. Il est logique, en effet, que les deux
enfants n'aient dit, ni l'un ni l'autre, la vérité, puisque
l'illusionniste vous avait prévenu qu'au moins l'un des deux
mentait - et si l'un mentait, l'autre ne pouvait pas avoir dit
la vérité ! Par conséquent, il n'y avait qu'une seule et unique
solution : les deux enfants mentaient. L'illusionniste vous
remet un nombre de Pièces d'Or équivalent à celui que vous aviez
misé. (N'oubliez pas d'ajouter cette somme à votre pécule.)
Ensuite, vous vous dirigez vers le comptoir pour demander une
chambre pour la nuit.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # Fait testé : « pari : N » posé au paragraphe 245 (N = mise) : l'illusionniste vous remet autant
    bets = [flag for flag in st.session_state.get("story_flags", []) if flag.startswith("pari : ")]
    if is_new_page() and bets:
        st.session_state["visibility_pari_gagne"] = int(bets[-1].split(": ")[1])
        for flag in bets:
            clear_flag(flag)
    if st.session_state.get("visibility_pari_gagne"):
        receive_gold(st.session_state["visibility_pari_gagne"], key="t6_62_gain")

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_253.py", label="253", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
