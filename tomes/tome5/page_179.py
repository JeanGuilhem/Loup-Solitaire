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

check_inventory(current_page_number=179, book=5)

fr_text = """
Les vitrines du magasin regorgent d'huiles, de potions, de
médicaments et d'étranges plantes exotiques de toutes sortes.
L'air est empli des effluves enivrantes des herbes médicinales.
Tout à coup, la foule s'agite au bout de la rue avant de disparaître
en un clin d'œil dans les magasins. Un homme se tient devant
vous : son visage est ruisselant de sueur et ses habits en
lambeaux sont recouverts de boue. C'est Maouk ! Il a survécu à
l'enfer du Baga-Darooz. « S'il n'y avait pas le Zakhan, je vous
aurais tué tout de suite, siffle-t-il entre ses dents avec un rictus
de haine. Mais je n'ai pas l'intention de perdre la tête pour un
lâche de votre espèce. » Vous pâlissez sous l'insulte, mais vous
parvenez à contenir votre colère. En effet, vous sentez qu'il ne
doit pas être seul et vous avez l'impression que des yeux vous
observent derrière chaque fenêtre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous voulez attaquer Maouk, rendez-vous au :'))
    st.page_link("tomes/tome5/page_197.py", label="197", icon="📄")

    st.write_stream(stream_text('Si vous préférez faire demi-tour et remonter la rue en courant, rendez-vous au :'))
    st.page_link("tomes/tome5/page_92.py", label="92", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
