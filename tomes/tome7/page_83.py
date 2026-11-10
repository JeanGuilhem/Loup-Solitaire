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

check_inventory(current_page_number=83, book=7)

fr_text = """
Le sarcophage est couvert de dessins compliqués, représentant
une procession de créatures surprenantes : certaines sont des
êtres mi-homme mi-bête, d'autres ne ressemblent à rien de ce
que vous avez pu rencontrer jusqu'à présent. L'un des dessins, en
particulier, retient votre attention : il s'agit d'un serpent lové
autour d'une rangée de trois boutons sculptés dans la pierre. Cela
vous rappelle une serrure de sécurité inventée par les Maîtres
Serruriers de Holmgard, votre ville natale. En poursuivant votre
inspection, votre œil averti découvre une mince fissure qui court
verticalement le long de la pierre. En suivant cette ligne, vous
comprenez qu'il s'agit du contour d'une porte dérobée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez essayer d'ouvrir cette porte secrète, rendez-vous au :"))
    st.page_link("tomes/tome7/page_115.py", label="115", icon="📄")

    st.write_stream(stream_text("Si vous préférez quitter le vestibule, vous pouvez sortir par le tunnel qui s'ouvre sur votre droite, rendez-vous au :"))
    st.page_link("tomes/tome7/page_323.py", label="323", icon="📄")

    st.write_stream(stream_text("Ou bien par le tunnel de gauche, rendez-vous dans ce cas au :"))
    st.page_link("tomes/tome7/page_201.py", label="201", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
