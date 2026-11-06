import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
    spend_gold,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=137, book=6)

fr_text = """
Une roulotte de paysan et un chariot de marchandises portant
pour emblème un Toa, arbre caractéristique de la région de
Casiorn, attendent devant les portes de la ville. Vous vous
placez derrière eux et vous patientez jusqu'à ce que les énormes
battants s'ouvrent enfin en grinçant sur leurs gonds. Un garde
surgit et, d'un geste, fait comprendre aux deux véhicules
d'entrer. Mais lorsque vous arrivez devant lui, il abaisse sa
lance de façon menaçante pour vous barrer le passage : « Le
droit d'entrée est de 3 Pièces d'Or, étranger. Payez ou partez !
»
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous acceptez de payer la taxe, donnez au garde les 3 Pièces d'Or qu'il exige et rendez-vous au 332."))
    if st.button("Payer 3 Pièces d'Or", key="taxe", disabled=st.session_state.purse < 3):
        if spend_gold(3):
            st.switch_page("tomes/tome6/page_332.py")
    st.page_link("tomes/tome6/page_332.py", label="332", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous ne voulez pas payer et si vous voulez tenter de contourner le garde pour entrer de force dans la ville, rendez-vous au :"))
    st.page_link("tomes/tome6/page_115.py", label="115", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
