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

check_inventory(current_page_number=300, book=4)

fr_text = """
Un hurlement d'épouvante et de douleur retentit. Le tireur isolé
s'abat sur le sol, sous le poids d'un Chien de Guerre qui vient de
lui sauter à la gorge. D'autres molosses attirés par ses cris
terrifiants se précipitent à leur tour, et l'homme est bientôt
déchiqueté par les crocs puissants des créatures sanguinaires.
Levant le regard, vous voyez un homme surgir de la barricade et
courir vers vous. Il porte un bouclier dans une main et un arc
dans l'autre. Vous le reconnaissez aussitôt : c'est le capitaine
Gayal. Hors d'haleine, il parvient jusqu'à vous et tire une flèche
de son carquois. Les Chiens de Guerre, lassés de leur victime,
cherchent à présent une autre proie et se dirigent vers vous. Le
capitaine vise et tire, puis prend une autre flèche dès qu'il a
relâché la corde de son arc. Les Chiens de Guerre s'effondrent sur
le sol, tout autour de vous, transpercés par les projectiles mortels
du capitaine Gayal. Ce dernier vous empoigne par le bras et vous
hisse sur son épaule d'un geste bref. Il vous emporte ensuite vers
la barricade. Des soldats du Sommerlund courent vers lui pour
l'aider, mais les archers ennemis sont maintenant à portée de tir
et vos compatriotes sont contraints de battre en retraite sous une
pluie de flèches. Les projectiles écarlates sifflent de tous côtés.
Finalement, vous atteignez la barricade. Des soldats écartent un
chariot, et le capitaine Gayal franchit la brèche en vous portant
toujours sur son épaule. Proche de l'épuisement, il chancelle, et
ses hommes se précipitent sur lui pour le soutenir avant qu'il ne
s'effondre sur le sol.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_341.py", label="341", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
