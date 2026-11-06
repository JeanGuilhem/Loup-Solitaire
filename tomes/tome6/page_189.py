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

check_inventory(current_page_number=189, book=6)

fr_text = """
Le marchand au visage émacié vous invite à vous asseoir à sa
table. Ses petits yeux malicieux brillent à l'idée de faire une
bonne affaire. Vous lui dites que vous souhaitez obtenir un
renseignement et que vous êtes prêt à payer, si toutefois le prix
est raisonnable. Aussitôt, il vous demande ce que vous voulez
savoir, mais lorsque vous lui répondez que vous désirez connaître
l'endroit où se trouve la rue des Chaudronniers, son visage
change brusquement d'expression.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_47.py", label="47", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
