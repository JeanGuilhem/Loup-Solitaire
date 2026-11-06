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

check_inventory(current_page_number=126, book=6)

fr_text = """
Une pluie de flèches s'abat sur la rive au moment où le
Capitaine ordonne à ses hommes de se mettre en ligne à
l'approche du pont de Tekaro. Les carcasses calcinées des tours
de siège se dressent sinistrement au-dessus des corps des
soldats gisant en tas devant les portes de la cité à moitié
enfoncées. Les remparts et les tourelles fortifiées du corps de
garde abritent une quantité invraisemblable d'archers et de
soldats prêts à déverser le plomb fondu et l'huile bouillante
contenus dans d'énormes chaudrons en cuivre qui luisent sous les
rayons du soleil couchant. « Chargez ! » hurle le Capitaine.
Vous êtes brutalement balayé par la horde des hommes et emporté
sur le pont dans un tourbillon de cavaliers déchaînés. A trente
mètres des portes, les archers commencent à tirer. Utilisez la
Table de Hasard pour obtenir un chiffre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    roll = hazard_roll(key="archers")
    if roll is not None:
        st.write_stream(stream_text("Si le nombre que vous avez tiré est compris entre 0 et 3, rendez-vous au :"))
        st.page_link("tomes/tome6/page_244.py", label="244", icon="📄", disabled=roll > 3)
        st.write_stream(stream_text("Si ce même nombre est compris entre 4 et 6, rendez-vous au :"))
        st.page_link("tomes/tome6/page_29.py", label="29", icon="📄", disabled=not 4 <= roll <= 6)
        st.write_stream(stream_text("S'il est compris entre 7 et 9, rendez-vous au :"))
        st.page_link("tomes/tome6/page_150.py", label="150", icon="📄", disabled=roll < 7)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
