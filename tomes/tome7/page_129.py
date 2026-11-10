import streamlit as st
from inventory import (
    add_to_inventory,
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    is_new_page,
    remove_from_inventory,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=129, book=7)

fr_text = """
Vous reconnaissez ces herbes: ce sont des feuilles d'Adgana, une
plante qui pousse en abondance au pied des collines de Bavari,
au nord du Dessi. Une seule dose suffira pour accroître votre
total d'HABILETÉ de 6 points, pour toute la durée d'un combat.
Néanmoins, vous devez savoir que la plupart des guerriers
professionnels se méfient grandement de l'Adgana et hésitent à
l'utiliser car elle crée une accoutumance ; pour cette raison, son
usage est généralement interdit dans de nombreux pays du
Magnamund. Si vous décidez d'en absorber une dose avant le
début d'un combat, il y a donc pour vous un risque de
dépendance. Dès la fin du combat, vous devrez alors utiliser la
Table de Hasard pour obtenir un chiffre. Si vous tirez 0 ou 1,
vous serez sous l'influence de cette drogue et vous devrez réduire
votre total d'ENDURANCE de 4 points. Cette diminution sera
définitive. Par ailleurs, si les événements à venir vous
contraignent à absorber une autre dose d'Adgana, son effet
positif sera moins grand que lors de la première prise: vous
n'augmenterez, dans ce cas, votre total d'HABILETÉ que de 3
points au lieu de 6 à l'origine.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # le Sachet d'Herbes (§56) devient une dose d'Adgana (+6 HABILETÉ pour un combat, cochée au début du combat)
    if is_new_page() and has_item("SACHET D'HERBES"):
        remove_from_inventory("SACHET D'HERBES")
        add_to_inventory("ADGANA")
    if has_item("ADGANA"):
        st.info("Votre Sachet d'Herbes est inscrit comme une dose d'Adgana. Après un combat où vous en aurez pris, tirez un chiffre sur la Table de Hasard : sur 0 ou 1, réduisez votre total d'ENDURANCE de 4 points.")

    st.write_stream(stream_text("Si vous souhaitez examiner le sarcophage, rendez-vous au :"))
    st.page_link("tomes/tome7/page_83.py", label="83", icon="📄")

    st.write_stream(stream_text("Si vous voulez plutôt vous engager dans le tunnel d'où les Rakhos ont surgi, rendez-vous au :"))
    st.page_link("tomes/tome7/page_323.py", label="323", icon="📄")

    st.write_stream(stream_text("Si vous préférez quitter le vestibule par l'autre tunnel, rendez-vous au :"))
    st.page_link("tomes/tome7/page_201.py", label="201", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
