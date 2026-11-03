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

check_inventory(current_page_number=214, book=4)

fr_text = """
Tandis que vous avancez dans le tunnel, un courant d'air humide
et froid vous frappe le visage. Les parois rocheuses sont
sillonnées de couches de minerai qui reflètent la lueur de votre
Torche en de multiples couleurs étincelantes. Vous commencez à
ressentir les effets de la fatigue. En outre, les lumières dansantes
qui vous entourent ont distrait votre attention. De ce fait, vous
n'avez pas remarqué que vous étiez en train de marcher sur des
champignons. Soudain, un nuage de spores roses s'élève. Aveuglé
et à moitié suffoqué, vous devez prendre une décision rapide
pour fuir cet endroit.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez courir le long du tunnel, rendez-vous au :'))
    st.page_link("tomes/tome4/page_46.py", label="46", icon="📄")

    st.write_stream(stream_text("Si vous préférez rebrousser chemin jusqu'à la salle que vous venez de quitter, afin de prendre le tunnel orienté au sud, rendez-vous au :"))
    st.page_link("tomes/tome4/page_117.py", label="117", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
