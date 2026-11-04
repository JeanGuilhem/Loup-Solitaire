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

check_inventory(current_page_number=195, book=5)

fr_text = """
Au centre d'une grande pièce circulaire, on a construit une forge
dont la cheminée s'enfonce en plein milieu du plafond. La
chaleur était déjà accablante, mais en pénétrant dans cette pièce,
vous avez réellement l'impression d'entrer dans un fourneau en
pleine activité. Deux hommes, torse nu, un pagne autour des
reins, manient un soufflet qui active la forge. Des gouttes de
sueur ruissellent sur leur peau et ils s'arrêtent fréquemment pour
boire de grandes rasades d'eau fraîche qu'ils tirent à l'aide d'une
louche d'un puits creusé sur le sol. Un Armurier au physique
impressionnant martèle une barre de fer chauffée à blanc posée
sur une enclume. Il a d'énormes épaules musclées et sa poitrine
est aussi large que les deux autres hommes réunis ! Soudain, les
hommes qui actionnaient le soufflet quittent la pièce, l'un par la
porte du mur nord, l'autre par la porte du mur ouest. Le grand
Armurier quant à lui, continue à battre le fer.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez suivre l'homme qui est sorti par la porte nord, rendez-vous au :"))
    st.page_link("tomes/tome5/page_11.py", label="11", icon="📄")

    st.write_stream(stream_text('Si vous préférez suivre celui qui a quitté la pièce par la porte ouest, rendez-vous au :'))
    st.page_link("tomes/tome5/page_146.py", label="146", icon="📄")

    st.write_stream(stream_text("Si vous désirez attaquer l'Armurier, rendez-vous au :"))
    st.page_link("tomes/tome5/page_190.py", label="190", icon="📄")

    st.write_stream(stream_text("Enfin, si vous voulez quitter la pièce et revenir sur vos pas pour emprunter l'autre couloir, rendez-vous au :"))
    st.page_link("tomes/tome5/page_30.py", label="30", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
