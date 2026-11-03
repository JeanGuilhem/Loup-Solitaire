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

check_inventory(current_page_number=298, book=4)

fr_text = """
Les Démons des Tunnels qui poussent de grands cris en se
recroquevillant sous vos coups disparaissent peu à peu.
Incrédule, vous secouez la tête et vous vous frottez les yeux avant
de vous rendre à l'évidence : il ne reste plus la moindre trace de
ces créatures, pas le moindre cadavre, en dépit des coups mortels
que vous leur avez portés. Vous comprenez alors ce qui s'est
passé. Les spores lâchées par les champignons ont provoqué en
vous une hallucination. Vos adversaires n'existaient que dans
votre tête. Malheureusement, tous les points d'ENDURANCE
que vous avez perdus au cours de ce combat imaginaire doivent
bel et bien être retranchés de votre total. En vous débattant avec
frénésie, vous vous êtes en effet heurté à plusieurs reprises
contre les aspérités pointues des parois du tunnel, vous infligeant
ainsi de véritables blessures. Vous rengainez à présent votre
arme et vous vous remettez en chemin d'un pas chancelant, en
vous éloignant le plus vite possible de ces champignons
maléfiques.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_185.py", label="185", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
