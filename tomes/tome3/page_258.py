import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    has_kai,
    remove_from_inventory,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=258, book=3)

fr_text = """
La sueur perle à votre front tandis que vous vous concentrez pour
essayer de vous protéger contre cette attaque psychique. Votre
agresseur, quel qu'il soit, est un adversaire redoutable et vous
êtes conscient qu'il va falloir vous débarrasser du Bracelet si vous
voulez survivre à l'épreuve de ce combat mental. Mais, pour
pouvoir ôter le Bracelet d'Or de votre poignet, vous allez devoir
pendant un instant relâcher votre concentration. Votre Bouclier
Psychique, dès lors, ne vous protégera plus. Utilisez la Table de Hasard pour obtenir un chiffre (en considérant
exceptionnellement que 0 = 10). Si vous maîtrisez la Discipline
Kaï de la Chasse ou celle du Sixième Sens, vous aurez le droit
d'ôter 2 au chiffre que la Table vous aura donné. Le total obtenu
vous indiquera le nombre de points d'ENDURANCE que vous
aurez perdu avant d'avoir réussi à vous débarrasser du Bracelet maudit.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    roll = hazard_roll()
    if roll is not None:
        value = roll if roll != 0 else 10
        if has_kai("La Chasse") or has_kai("Le Sixième Sens"):
            loss = max(0, value - 2)
            st.write(f"*Grâce à votre Discipline Kaï, vous ôtez 2 au chiffre tiré : {value} - 2 = {loss}.*")
        else:
            loss = value
        if "hazard_bracelet_done" not in st.session_state:
            st.session_state["hazard_bracelet_done"] = True
            if has_item("BRACELET D'OR"):
                remove_from_inventory("BRACELET D'OR")
            change_endurance(-loss)
        st.metric(label="Endurance", value=st.session_state.endurance, delta=-loss)
        st.write_stream(stream_text("Vous vous êtes débarrassé du Bracelet maudit. Rendez-vous au :"))
        st.page_link("tomes/tome3/page_63.py", label="63", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
