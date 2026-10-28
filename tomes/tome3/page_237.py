import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies, handle_repas

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=237, book=3)

fr_text = """
Vous arrivez bientôt au pied d'un large escalier de pierre qui
monte en direction du nord vers un palier situé à une dizaine de
mètres au-dessus de vous. Chaque marche a été légèrement
creusée en son milieu par les pieds des innombrables créatures
qui ont jadis habité les étages inférieurs de la forteresse. Tandis
que vous escaladez ces mêmes marches, vous vous demandez
pendant combien de temps encore vous pourrez éviter que votre
présence ne soit découverte. Jusqu'à présent vous n'avez pas
rencontré âme qui vive dans ces couloirs déserts. Pour l'instant,
vous bénéficiez de l'effet de surprise et vous priez le ciel que
Vonotar ne soupçonne pas la présence d'un intrus dans les
profondeurs de sa propre forteresse. Vous arrivez bientôt sur le
palier, puis vous traversez une grotte vide en vous dirigeant vers
une arcade plongée dans la pénombre. Là, le couloir bifurque :
un passage part vers l'est, un autre vers l'ouest. Vous êtes affamé
et il vous faut à présent prendre un Repas, sinon vous perdrez 3
points d'ENDURANCE.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    handle_repas()
    st.write_stream(stream_text("Si vous souhaitez emprunter le passage orienté à l'est, rendez-vous au :"))
    st.page_link("tomes/tome3/page_92.py", label="92", icon="📄")
    st.write_stream(stream_text("Si vous préférez vous engager dans le passage orienté à l'ouest, rendez-vous au :"))
    st.page_link("tomes/tome3/page_297.py", label="297", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
