import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=41, book=2)

fr_text = """
Vous avez de la chance car votre signal de détresse a été aperçu par
l'équipage du bateau qui met à présent le cap dans votre direction. C'est
un petit bateau de pêche en provenance du port de Ragadorn. Les
pêcheurs qui sont à bord ont une mine plutôt patibulaire, mais ils se
montrent amicaux avec vous ; ils vous donnent une couverture pour
vous réchauffer et vous offrent de quoi manger. Le capitaine vous
conseille de faire un somme pendant les trois heures que durera le
voyage de retour à Ragadorn.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous décidez de suivre ce conseil, reprenez un point d'ENDURANCE et rendez-vous au :"))
    if st.button("Dormir (+1 point d'ENDURANCE) et se rendre au 194"):
        change_endurance(1)
        st.switch_page("tomes/tome2/page_194.py")
    st.write_stream(stream_text("Si vous préférez rester éveillé et scruter la mer dans l'espoir de retrouver d'autres survivants du naufrage, rendez-vous au :"))
    st.page_link("tomes/tome2/page_251.py", label="251", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
