import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=180, book=3)

fr_text = """
Dans l'obscurité balayée de neige, vous distinguez deux petits
points rouges et brillants qui grandissent peu à peu. Puis
soudain, une forme se dessine dans l'ombre : vous voyez alors
apparaître une grande et hideuse créature quadrupède qui
bondit sur vous. Elle a les yeux étincelants et ouvre une gueule
hérissée de dents, exhibant en même temps une énorme langue
couverte de poils rêches qu'elle pointe en direction de votre
visage. « Argh ! Un Languabarb ! » s'écrie Fenor. Il se précipite
aussitôt à votre côté en brandissant une épée dont il essaie de
frapper la langue de la créature. L'animal, cependant, est déjà sur
vous et il vous faut le combattre. Indifférente à l'attaque de
Fenor, la bête monstrueuse ne semble s'intéresser qu'à vous.
Fenor lui porte ses coups par-derrière et ne sera donc pas blessé.
En revanche, il fera perdre 3 points supplémentaires
d'ENDURANCE à votre adversaire, et cela à chaque Assaut, en
raison des blessures qu'il lui inflige.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("LANGUABARB", 11, 35)], stop_when_wounded=True, ally_damage=3)
    if outcome == "win":
        st.write_stream(stream_text("Vous avez tué la créature sans perdre aucun point d'ENDURANCE, rendez-vous au :"))
        st.page_link("tomes/tome3/page_70.py", label="70", icon="📄")
    elif outcome == "wounded":
        st.write_stream(stream_text("Vous avez perdu des points d'ENDURANCE au cours du combat, rendez-vous immédiatement au :"))
        st.page_link("tomes/tome3/page_129.py", label="129", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
