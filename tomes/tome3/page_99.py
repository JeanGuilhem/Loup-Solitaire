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

check_inventory(current_page_number=99, book=3)

fr_text = """
Lorsque vous tirez de son fourreau le puissant Glaive de
Sommer, un flamboiement doré illumine l'obscurité du passage.
Le Monstre d'Enfer recule d'un pas en poussant un hurlement,
ses yeux rouges brillant de haine et de terreur. Il a reconnu en
effet l'arme que vous brandissez et il sait que son pouvoir peut le
détruire à jamais. Dans une tentative désespérée, le Monstre
d'Enfer vous attaque en faisant usage de sa terrible Puissance
Psychique. A moins que vous ne maîtrisiez la Discipline Kaï du
Bouclier Psychique, vous perdrez 2 points d'ENDURANCE
supplémentaires à chaque Assaut (si, lors d'un Assaut, la Table
des Coups Portés vous indique que vous ne subissez pas de perte
d'ENDURANCE, il vous faudra malgré tout retrancher ces 2
points). Votre adversaire, lui, est insensible à la Puissance
Psychique d'autrui mais en revanche, en tant que mort vivant, il
est particulièrement vulnérable aux coups du Glaive de Sommer.
Aussi aurez-vous le droit de doubler tous les points
d'ENDURANCE perdus par la créature au cours de ce combat.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("MONSTRE D'ENFER", 22, 30)], psychic_immune=True, psychic_damage=2, undead=True)
    if outcome == "win":

        st.write_stream(stream_text("Si vous sortez vainqueur de l'affrontement, rendez-vous au :"))
        st.page_link("tomes/tome3/page_230.py", label="230", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
