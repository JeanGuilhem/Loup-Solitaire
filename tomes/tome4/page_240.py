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

check_inventory(current_page_number=240, book=4)

fr_text = """
La rivière poursuit son cours en direction du sud sur plus de 15
kilomètres. Vous traversez plusieurs grottes, mais les berges
rocheuses sont trop escarpées pour que vous puissiez aborder.
Alors que vous ramez le long d'un tunnel particulièrement large,
vous vous rendez compte soudain que le bateau avance de plus
en plus vite. Au loin, vous entendez le faible grondement d'une
eau bouillonnante. Le bruit augmente peu à peu d'intensité, et
bientôt c'est un véritable vacarme qui retentit dans le tunnel.
Vous vous préparez à traverser de forts remous, mais vous ne
vous attendiez pas au spectacle qui s'offre soudain à vos yeux. A
moins de 15 mètres en effet, la rivière disparaît dans les
profondeurs d'une immense chute d'eau. Vos hommes tentent
désespérément de ramer contre le courant pour essayer
d'atteindre une paroi du tunnel. Leurs efforts restent vains
cependant et le bateau est emporté jusqu'à la chute d'eau.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Utilisez la Table de Hasard pour obtenir un chiffre.'))
    roll = hazard_roll()
    if roll is not None:
        if roll <= 4:
            st.write_stream(stream_text('Si vous tirez un chiffre de 0 à 4, rendez-vous au :'))
            st.page_link("tomes/tome4/page_94.py", label="94", icon="📄")
        else:
            st.write_stream(stream_text('De 5 à 9, rendez-vous au :'))
            st.page_link("tomes/tome4/page_158.py", label="158", icon="📄")


    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
