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

check_inventory(current_page_number=202, book=6)

fr_text = """
C'est une petite chambre minable et sans meubles, à part un
matelas en paille défoncé reposant à même le sol et un vieux
tapis effrangé. Vous fermez la porte à clef et vous vous installez
pour la nuit. Vous vous endormez la tête sur votre Sac à Dos et
avec votre manteau en guise de couverture. Mais vous êtes
brusquement réveillé au milieu de la nuit par une puissante
lumière. Une étoile filante d'une luminosité exceptionnelle décrit
un arc de cercle au-dessus de la ville et illumine au passage les
mornes alentours d'une lumière riche et colorée. Vous regardez
l'étoile disparaître à l'horizon, puis vous retournez vous coucher
car vous tombez de sommeil. Quelques heures plus tard, vous
entendez la cloche de l'auberge sonner à toute volée, alors que
vous avez l'impression que vous venez à peine de fermer les yeux.
« Debout tout le monde ! Debout ! Le jour vient de se lever,
debout, bonnes gens ! » Tandis que la voix de l'aubergiste
résonne à travers l'auberge, vous rassemblez votre équipement
puis vous allez chercher votre cheval à l'écurie. Le sommeil
réparateur vous fait regagner 3 points d'ENDURANCE. Inscrivez
votre nouveau total sur votre Feuille d'Aventure avant de partir à
la recherche de la rue des Chaudronniers.
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
