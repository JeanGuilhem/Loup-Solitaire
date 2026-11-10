import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=241, book=7)

fr_text = """
Un éclair rouge passe en sifflant au-dessus de votre tête et
explose juste à l'entrée du tunnel. Des éclats de pierre vous
égratignent le crâne et vous courez à travers les débris, aveuglé
pendant un court instant. Au moment où vous levez les bras pour
vous essuyer le visage avec votre manche, un autre éclair jaillit et
vous atteint en plein dos. Vous tombez à plat ventre sur le sol du
tunnel.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous maîtrisez la Discipline Magnakaï de la Science Médicale, ôtez 1 point au chiffre tiré. Ce chiffre représente le nombre de points d'ENDURANCE que vous avez perdus lors de cette attaque."))
    roll = hazard_roll(key="eclair")
    if roll is not None:
        loss = max(0, roll - (1 if has_magnakai("Science Médicale") else 0))
        if not st.session_state.get("hazard_eclair_done"):  # clé hazard_* : remise à zéro à chaque visite
            st.session_state["hazard_eclair_done"] = True
            change_endurance(-loss)
        st.metric(label="Endurance", value=st.session_state.endurance, delta=-loss)
        st.write_stream(stream_text("Vous essayez de surmonter votre douleur et vous vous relevez péniblement. Vous reprenez ensuite votre chemin le long du tunnel enfumé. Rendez-vous au :"))
        st.page_link("tomes/tome7/page_277.py", label="277", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
