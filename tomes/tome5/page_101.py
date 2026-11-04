import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    pickup_gold,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=101, book=5)

fr_text = """
L'homme pousse un cri puis s'effondre sur le sol en gémissant
avant d'exhaler son dernier souffle. Pendant ce temps, l'autre
Garde s'est enfui précipitamment en oubliant son arme. Vous
vous lancez aussitôt à sa poursuite, vous arrêtant seulement pour
ramasser le trident. Vous devez absolument l'arrêter avant qu'il
ne prévienne les autres sentinelles. Vous levez le trident au-dessus
de votre tête puis vous le lancez dans sa direction. L'arme
l'atteint en plein milieu du dos, le projetant en avant. Il meurt
avant même d'avoir touché le sol.
En fouillant les cadavres vous découvrez les objets suivants : 4
Pièces d'Or, 1 Poignard, 1 Epée et 1 Potion d'Alether (qui
augmente de deux points votre total d'HABILETÉ pour la durée
d'un combat). Vous pouvez également prendre la Sarbacane et
les Fléchettes de Sommeil qui n'ont pas été utilisées. Si vous
désirez prendre l'un ou l'autre de ces objets, n'oubliez pas de le
noter sur votre Feuille d'Aventure dans la case Sac à Dos.
"""

fr_text_2 = """
Dans les vêtements de l'homme à la Sarbacane, vous trouvez un petit
morceau de parchemin sur lequel sont inscrits la date du jour et
le chiffre 67. Un sourire illumine votre visage lorsque vous
comprenez qu'il s'agit du chiffre qui vous permettra d'ouvrir la
porte de bronze. Vous retenez votre respiration puis vous
composez le numéro.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_gold(4, key="gold")
    pickup_button("POIGNARD", key="poignard", label="Prendre le Poignard")
    pickup_button("ÉPÉE", key="epee", label="Prendre l'Épée")
    pickup_button("FIOLE D'ALÉTHER", key="alether", label="Prendre la Potion d'Alether")
    pickup_button("SARBACANE", key="sarbacane", label="Prendre la Sarbacane")
    pickup_button("FLÈCHE DE SOMMEIL", key="fleches", label="Prendre les Fléchettes de Sommeil")

    st.write(fr_text_2)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_67.py", label="67", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
