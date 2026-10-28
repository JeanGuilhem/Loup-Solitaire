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

check_inventory(current_page_number=336, book=3)

fr_text = """
Au bout d'une vingtaine de mètres, vous arrivez au pied d'un
escalier dont vous montez les marches. Parvenu au sommet, vous
apercevez un peu plus loin une faible lumière qui se répand sur le
sol malpropre d'un nouveau couloir. Vous vous approchez de
cette lueur et vous découvrez une ouverture aménagée dans la
paroi. En regardant au travers, vous apercevez un vieil homme
recroquevillé dans le coin d'une cellule, à 5 ou 6 mètres en
contrebas. Ses cheveux sont longs et emmêlés et la saleté dont sa
toge est incrustée a presque effacé les croissants de lune et les
étoiles brodés sur l'étoffe.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez appeler ce vieil homme, rendez-vous au :"))
    st.page_link("tomes/tome3/page_247.py", label="247", icon="📄")
    st.write_stream(stream_text("Si vous préférez poursuivre votre chemin le long du couloir, rendez-vous au :"))
    st.page_link("tomes/tome3/page_30.py", label="30", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
