import streamlit as st
from inventory import (
    buy_button,
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

check_inventory(current_page_number=2, book=6)

fr_text = """
Certains de ces flacons contiennent des potions qui pourront vous
être utiles lors de votre voyage. Vous parcourez des yeux les
innombrables fioles qui s'alignent sur les étagères et vous en
lisez attentivement les étiquettes :

- Potion de Laumspur (Chaque dose redonne 4 points d'ENDURANCE.) :
5 Pièces d'Or;
- Potion d'Herbe à Potence (Chaque dose procure un sommeil d'une
ou deux heures.) : 2 Pièces d'Or;
- Elixir de Rendalim (Chaque dose fait gagner 6 points
d'ENDURANCE.) : 7 Pièces d'Or;
- Potion d'Alether (augmente le total d'ENDURANCE de 2 points pour
toute la durée du combat) : 4 Pièces d'Or;
- Concentré de Chiendent des Cimetières (Son absorption provoque
une mort instantanée.) : 4 Pièces d'Or.

Vous pouvez acheter les potions que vous désirez. Dans ce cas,
n'oubliez pas de rayer les Pièces d'Or que vous aurez dépensées et
d'inscrire vos achats dans la case Sac à Dos de votre Feuille
d'Aventure.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    buy_button("POTION DE LAUMSPUR", 5, key="laumspur_1", label="Acheter une Potion de Laumspur (5 Couronnes)")
    buy_button("POTION DE LAUMSPUR", 5, key="laumspur_2", label="Acheter une autre Potion de Laumspur (5 Couronnes)")
    buy_button("POTION D'HERBE À POTENCE", 2, key="potence", label="Acheter une Potion d'Herbe à Potence (2 Couronnes)")
    buy_button("ÉLIXIR DE RENDALIM", 7, key="rendalim_1", label="Acheter un Élixir de Rendalim (7 Couronnes)")
    buy_button("ÉLIXIR DE RENDALIM", 7, key="rendalim_2", label="Acheter un autre Élixir de Rendalim (7 Couronnes)")
    # le livre parle ici d'ENDURANCE, mais la Potion d'Alether donne +2 HABILETÉ pour un combat
    buy_button("FIOLE D'ALÉTHER", 4, key="alether", label="Acheter une Potion d'Alether (4 Couronnes)")
    buy_button("CONCENTRÉ DE CHIENDENT DES CIMETIÈRES", 4, key="chiendent", label="Acheter un Concentré de Chiendent des Cimetières (4 Couronnes)")

    st.write_stream(stream_text("Si vous souhaitez aller voir ce que les autres magasins de la rue ont à proposer, rendez-vous au :"))
    st.page_link("tomes/tome6/page_152.py", label="152", icon="📄")

    st.write_stream(stream_text("Si vous préférez attendre que le Capitaine en ait fini avec ses achats, rendez-vous au :"))
    st.page_link("tomes/tome6/page_231.py", label="231", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
