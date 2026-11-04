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

check_inventory(current_page_number=258, book=5)

fr_text = """
Le Glaive de Sommer vibre de puissance lorsque vous le pointez
vers la flamme qui s'approche rapidement en émettant un
sifflement si fort qu'il couvre le bruit de la bataille. Vous vous
arc-boutez en attendant l'impact. La flamme heurte le Glaive de
Sommer dans un bruit de tonnerre et se fixe au bout de la lame
magique en formant une boule de feu rougeoyante.
Instinctivement, vous faites tourner le Glaive au-dessus de votre
tête et vous lancez la boule de feu vers le ciel. Le Vordak hurle de
terreur, mais il est trop tard et son destin est fixé : la boule de feu
embrase le Zlan et son cavalier dans une gigantesque explosion,
brillante comme la lumière du soleil.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_267.py", label="267", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
