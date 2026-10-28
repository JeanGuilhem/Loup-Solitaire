import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies, ls_death

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=175, book=3)

fr_text = """
Vous faites un pas de côté pour esquiver la créature et vous lui
portez à la tête un coup qui aurait mis hors de combat n'importe
quel mortel. Mais, à votre grand dam, le Monstre d'Enfer est
indemne et se lance à nouveau à l'attaque. C'est un mort vivant
aux pouvoirs redoutables, invulnérable aux armes normales. Les
Maîtres des Ténèbres l'ont envoyé ici en mission pour tuer
Vonotar et le punir ainsi de sa défaite dans la bataille du golfe de
Holm. A présent qu'il est libéré du pentagramme qui
l'emprisonnait, le Monstre d'Enfer peut accomplir sa mission et
retourner chez lui pour y recevoir de ses maîtres récompenses et
honneurs. Vous hurlez de terreur lorsque les doigts de la créature
s'enfoncent dans les chairs de votre cou, mais vos hurlements ne
sont entendus de personne dans ce sombre couloir et seule la
mort mettra un terme à l'insupportable douleur qui vous étreint
la gorge. Votre mission s'achève ici en même temps que votre vie.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    show_illustrations()
    ls_death()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
