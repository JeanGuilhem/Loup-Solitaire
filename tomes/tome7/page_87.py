import streamlit as st
from inventory import (
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

check_inventory(current_page_number=87, book=7)

fr_text = """
« Surtout, restez près de moi ! » crie le guerrier par-dessus son
épaule, tandis que vous courez tous deux sur le pont, les
créatures sur vos talons. Les événements se déroulent trop vite
pour que vous puissiez raisonner avec sang-froid ; pour l'instant,
c'est l'instinct seul qui vous guide. Une fois arrivé à l'entrée du
passage, votre compagnon s'arrête pile, se retourne et vous
repousse brutalement des deux mains. La collision vous coupe le
souffle, mais vous sentez qu'il vous retient par votre Sac à Dos et
vous empêche de tomber à la renverse. « Attention, c'est un piège ! s'écrie-t-il en désignant une dalle en pierre devant vous. Maudit
soit cet endroit infernal ! Trouverons-nous jamais un lieu sûr,
hors de portée de la diablerie de Zahda ? » Comme en réponse à
ses paroles, un sinistre ricanement retentit soudain derrière vous ; les créatures sont plus proches que vous ne le pensiez. « Sautez
vite, par pitié, sautez ! » implore votre compagnon.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez sauter par-dessus la dalle, rendez-vous au :"))
    st.page_link("tomes/tome7/page_268.py", label="268", icon="📄")

    st.write_stream(stream_text("Si vous préférez rester sur place et attendre l'ennemi de pied ferme, rendez-vous au :"))
    st.page_link("tomes/tome7/page_299.py", label="299", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
