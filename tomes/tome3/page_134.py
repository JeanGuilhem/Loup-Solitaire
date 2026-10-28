import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=134, book=3)

fr_text = """
Le lendemain à l'aube, lorsque vous vous réveillez, Fenor est en
train de préparer le petit déjeuner. Il vous tend alors un bol
fumant et vous ne vous faites guère prier pour en avaler le
contenu. Vous chargez ensuite le matériel sur les traîneaux avant
de reprendre votre chemin. C'est une belle matinée. Le vent est
tombé et l'air est frais et limpide. Les chiens Kanu, débordant
d'énergie, sont impatients de repartir. Pendant la plus grande
partie de votre trajet, la glace est lisse et vous avancez sans
difficulté. A la nuit tombée, vous avez atteint l'île de Syem, un pic
de granit qui s'élève à 120 mètres au-dessus de la banquise.
Vous établissez votre campement du côté sous le vent pour
essayer de vous protéger le mieux possible d'éventuelles
tempêtes nocturnes.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    number = hazard_roll()
    if number is not None and number <= 3:
        st.write_stream(stream_text("Rendez-vous au :"))
        st.page_link("tomes/tome3/page_57.py", label="57", icon="📄")
    elif number is not None and number <= 6:
        st.write_stream(stream_text("Rendez-vous au :"))
        st.page_link("tomes/tome3/page_188.py", label="188", icon="📄")
    elif number is not None:
        st.write_stream(stream_text("Rendez-vous au :"))
        st.page_link("tomes/tome3/page_331.py", label="331", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
