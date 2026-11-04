import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=35, book=5)

fr_text = """
Le grand serpent à l'agonie se tord et se convulse en tous sens.
L'odeur fétide du sang noir et épais qui s'écoule de ses plaies
vous soulève le cœur et c'est en serrant les dents et en retenant
votre souffle que vous soulevez le cadavre du Yas pour regarder
dans le coffre. Celui-ci renferme six masses d'armes finement
ouvragées et incrustées de rubis, d'émeraudes et de perles. Dans
les Contrées du Nord la valeur de ces armes serait inestimable !
Au fond du coffre, vous découvrez également une petite Clé de
Cuivre. Si vous souhaitez prendre une masse d'armes incrustée
de pierreries, la Clé de Cuivre, ou bien ces deux objets, inscrivez-les sur votre Feuille d'Aventure dans la case des Objets Spéciaux.
Si vous prenez la Clé de Cuivre, vous devrez la mettre dans l'une
des poches de votre tunique ; quant à la masse d'armes, vous
devrez la glisser à votre ceinture. Les vapeurs acides qui se
dégagent du sang du serpent commencent à vous suffoquer. Vous
montez rapidement les marches en pierre et vous quittez
l'Armurerie par la porte nord.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_button("MASSE D'ARMES INCRUSTÉE", key="masse", label="Prendre une masse d'armes incrustée de pierreries")
    pickup_button("CLÉ DE CUIVRE", key="cle", label="Prendre la Clé de Cuivre")

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome5/page_14.py", label="14", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
