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

check_inventory(current_page_number=348, book=4)

fr_text = """
Moins de 50 mètres plus loin, vous apercevez un levier fixé à la
paroi du tunnel. Votre instinct de Seigneur Kaï vous incite à la
méfiance et, soupçonnant un traquenard, vous examinez
soigneusement le sol pour essayer d'y découvrir un piège
éventuel. Vous ne trouvez rien, cependant. Mais en levant les
yeux, vous remarquez, entre deux poutres, la partie inférieure
d'une large herse. Vous tirez le levier et la herse s'abat aussitôt,
bloquant le tunnel derrière vous. Pour être certain que personne
ne pourra vous suivre, vous brisez le levier à l'aide d'une grosse
pierre avant de continuer votre chemin le long du souterrain.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome4/page_185.py", label="185", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
