import streamlit as st
from inventory import (
    check_inventory,
    clear_flag,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
    spend_gold,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=113, book=6)

fr_text = """
Ce n'est pas la bonne réponse : en effet, l'illusionniste avait
précisé qu'au moins l'un des deux enfants mentait. Et si l'un
mentait, l'autre ne pouvait donc pas avoir dit la vérité. La
réponse exacte est que les enfants mentaient tous les deux. Vous
avez malheureusement perdu tout l'argent que vous aviez misé
(rayez les Pièces d'Or perdues au jeu sur votre Feuille
d'Aventure). Après cette désagréable déconvenue, vous vous
dirigez vers le comptoir afin de demander une chambre pour la
nuit.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # Fait testé : « pari : N » posé au paragraphe 245 (N = mise) : la mise est perdue
    bets = [flag for flag in st.session_state.get("story_flags", []) if flag.startswith("pari : ")]
    if is_new_page() and bets:
        st.session_state["visibility_pari"] = min(int(bets[-1].split(": ")[1]), st.session_state.purse)
        spend_gold(st.session_state["visibility_pari"])
        for flag in bets:
            clear_flag(flag)
    if st.session_state.get("visibility_pari"):
        st.write(f"*Vous perdez votre mise : {st.session_state['visibility_pari']} Pièce(s) d'Or.*")

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_253.py", label="253", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
