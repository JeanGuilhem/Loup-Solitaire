import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, ls_death

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=259, book=5)

fr_text = """
Deux flèches fendent l'air en sifflant et viennent vous frapper
dans le dos. Alors qu'une douleur insupportable vous vrille le
corps, vous vous évanouissez et vous tombez sur les pointes
empoisonnées. Tandis que votre sang s'écoule à flots, le dernier
bruit que vous entendez est le rire hideux et sarcastique du
Seigneur des Ténèbres Haakon s'élevant au-dessus des
hurlements macabres de ses cruels guerriers Drakkars. Votre vie
s'achève ici et tous les espoirs pour la survie du Sommerlund
sont désormais anéantis.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    show_illustrations()
    ls_death()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
