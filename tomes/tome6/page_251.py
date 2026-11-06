import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=251, book=6)

fr_text = """
La chambre vous déçoit énormément ; pour 5 Pièces d'Or, vous vous
attendiez à quelque chose de plus luxueux, et l'ameublement et le
confort laissent vraiment à désirer. Dans un coin de la pièce, de
la vapeur s'échappe d'une barrique et enfume la chambre. Vous
pensez tout d'abord qu'il s'agit d'une installation pour le
chauffage mais, en vous approchant, vous découvrez que le tonneau
est plein d'eau savonneuse. Votre bain est prêt ! Vous prenez
votre bain avant de vous installer pour une bonne nuit de sommeil.
Mais au beau milieu de la nuit, vous êtes réveillé par une lumière
extrêmement vive. Une étoile filante est en train de passer
au-dessus de la ville, décrivant un arc de cercle. Au passage,
elle illumine la cité et votre chambre est inondée de lumière
irisée. Vous regardez par la fenêtre l'étoile qui disparaît
lentement à l'horizon, puis vous vous rendormez. Quelques heures
plus tard, vous êtes réveillé en sursaut par la cloche grinçante
de l'auberge, mais vous avez l'impression que vous venez juste de
vous endormir. « Debout, debout tout le monde ! Un nouveau jour
vient de se lever, debout, braves gens ! » Tandis que la voix de
l'aubergiste résonne dans l'auberge, vous rassemblez votre
équipement et vous allez chercher votre cheval à l'écurie. Cette
nuit de repos vous fait regagner 3 points d'ENDURANCE. Faites les
modifications nécessaires sur votre Feuille d'Aventure avant de
partir pour la rue des Chaudronniers.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(3)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=3)
    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_300.py", label="300", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
