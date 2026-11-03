import streamlit as st
from combat import combat
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

check_inventory(current_page_number=196, book=4)

fr_text = """
Un éclair déchire le ciel d'orage, illuminant les silhouettes des
brigands qui se glissent dans les écuries. Accroupi sur le balcon,
vous faites signe à vos hommes de se préparer. Vous sautez alors
sur le toit de l'écurie mais les tuiles d'argile sont trop minces
pour supporter votre poids et vous passez à travers et atterrissez
dans une botte de foin. Par chance, vous êtes indemne et vous
vous relevez aussitôt, mais un brigand se tient devant vous à
moins d'un mètre, l'épée brandie, prête à s'abattre sur votre tête.
Il faut vous défendre contre ce Guerrier Pillard.

Il vous est impossible de prendre la fuite et vous devrez donc
affronter votre adversaire jusqu'à la mort de l'un de vous deux.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("GUERRIER PILLARD", 16, 23)])
    if outcome == "win":
        st.write_stream(stream_text('Si vous êtes vainqueur, rendez-vous au :'))
        st.page_link("tomes/tome4/page_217.py", label="217", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
