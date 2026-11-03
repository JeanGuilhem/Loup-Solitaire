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

check_inventory(current_page_number=140, book=4)

fr_text = """
L'obscurité du crépuscule enveloppe l'avant-poste assiégé de
Ruanon et vous profitez de la nuit pour traverser la plaine
jonchée de cadavres en direction du sud. Une ancienne route
mène à Maaken, mais elle est contrôlée par les Guerriers
vassagoniens. Ils y sont rassemblés par groupes, soignant leurs
blessés et ruminant leur défaite. Bien qu'ils soient abattus et
démoralisés, ils n'en restent pas moins des ennemis mortels et il
serait trop dangereux d'essayer de franchir leurs lignes ; il vous
faut donc passer par la forêt pour pouvoir vous cacher.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez pénétrer dans la forêt à droite de la route, rendez-vous au :'))
    st.page_link("tomes/tome4/page_70.py", label="70", icon="📄")

    st.write_stream(stream_text('Si vous préférez traverser la forêt du côté gauche, rendez-vous au :'))
    st.page_link("tomes/tome4/page_314.py", label="314", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
