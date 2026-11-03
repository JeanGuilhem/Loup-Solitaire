import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=345, book=4)

fr_text = """
En vérifiant les stalles de l'écurie, vous découvrez qu'il ne vous
reste plus que onze chevaux ; les autres ont été volés par les
brigands. Après avoir mûrement réfléchi, vous décidez de
prendre dix hommes avec vous pour continuer votre mission et
de renvoyer les autres patrouilleurs à Holmgard dès l'aube, pour
faire un rapport détaillé de la situation. Lorsque le jour se lève,
ils partent à pied en direction du nord et vous les regardez
s'éloigner ; puis, lorsqu'ils ont disparu, vous vous tournez dans la
direction opposée et vous poursuivez votre chemin en compagnie
des dix patrouilleurs.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre."))
    roll = hazard_roll()
    if roll is not None:
        if roll <= 6:
            st.write_stream(stream_text("Si vous tirez un chiffre de 0 à 6, rendez-vous au :"))
            st.page_link("tomes/tome4/page_51.py", label="51", icon="📄")
        else:
            st.write_stream(stream_text("De 7 à 9, rendez-vous au :"))
            st.page_link("tomes/tome4/page_120.py", label="120", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
