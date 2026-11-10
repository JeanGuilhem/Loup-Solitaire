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

check_inventory(current_page_number=244, book=7)

fr_text = """
Votre Maîtrise du Cercle de Savoir vous permet de comprendre
l'étrange langage de ces créatures et vous écoutez, tapi dans
l'ombre, leur conversation. « Les réparations dans le puits
central sont presque terminées. Dans trois soleils, nous serons en
mesure de continuer les travaux », dit une voix flûtée. « Nous ne
pouvons pas attendre si longtemps, l'interrompt une autre voix,
plus profonde, avec un accent de colère. Le Seigneur Zahda a
ordonné que le percement reprenne sans délai. Nous devons
obéir à ses ordres. » « Mais les risques sont trop élevés, rétorque
la première voix. Nous avons déjà perdu cent esclaves dans les
inondations. La prochaine fois, nous ne perdrons pas que des
esclaves ! » Un bruit dans le couloir vous avertit d'un danger
imminent : une patrouille de gardes armés s'avance dans votre
direction.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez vous faufiler dans la pièce jusqu'au couloir de l'autre côté, en essayant de ne pas vous faire voir, rendez-vous au :"))
    st.page_link("tomes/tome7/page_343.py", label="343", icon="📄")

    st.write_stream(stream_text("Si vous préférez vous cacher dans l'embrasure de la porte, rendez-vous au :"))
    st.page_link("tomes/tome7/page_181.py", label="181", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
