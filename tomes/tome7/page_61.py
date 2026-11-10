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

check_inventory(current_page_number=61, book=7)

fr_text = """
Votre lumière brille avec éclat dans le passage sombre et humide.
Vous découvrez, juste devant vous, l'entrée d'une caverne dont la
voûte s'orne d'une multitude de stalactites d'un blanc laiteux, qui
pendent comme une armée de lances acérées. Vous traversez
prudemment la grotte, les nerfs à fleur de peau, car vous
percevez d'étranges bruits dans la pénombre. Vous vous frayez
ensuite un chemin à travers un dédale de souterrains, glissant
sur les dalles couvertes de mousse et vous égratignant
fréquemment contre les aspérités de la paroi, puis vous arrivez à
une pièce aux murs parfaitement lisses, taillés avec précision
dans le roc noir. Il y a un escalier partant d'une arche sur la
gauche et, droit devant vous, une grosse porte en pierre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez aller examiner cette porte, rendez-vous au :"))
    st.page_link("tomes/tome7/page_274.py", label="274", icon="📄")

    st.write_stream(stream_text("Si vous préférez monter l'escalier sur votre gauche, rendez-vous au :"))
    st.page_link("tomes/tome7/page_193.py", label="193", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
