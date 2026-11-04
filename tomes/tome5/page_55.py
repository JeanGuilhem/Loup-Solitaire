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

check_inventory(current_page_number=55, book=5)

fr_text = """
La température augmente régulièrement et vous êtes en nage.
Devant vous se trouve une pièce emplie d'une vapeur épaisse qui
s'élève du sol en ébullition. Au moment où vous vous apprêtez à
entrer dans cette pièce, vous prenez conscience du danger qui
vous guette : le trottoir en pierre s'interrompt brusquement après
quelques mètres. En contrebas, vous découvrez ce qui vous
semble tout d'abord être la surface d'un énorme chaudron
bouillonnant. En réalité, il s'agit d'un tar-sorkh : un geyser de
boue ! Ce genre de phénomène est assez courant en Vassagonie.
Le sol de ce pays désertique est instable et des secousses
sismiques l'ébranlent fréquemment, mais elles sont légères et
n'entraînent jamais de graves conséquences. Les Vassagoniens
appellent ces tremblements de terre Tasa-Dophiem, le Combat
des Dieux. Par ailleurs, ces geysers de boue ont fini par être
utilisés pour fournir une chaleur constante dans les maisons
construites au-dessus d'eux. La vapeur s'élevant d'un tar-shorkh
est canalisée dans de grosses cheminées circulaires qui, à leur
tour, dispensent la chaleur à travers les habitations grâce à un
réseau de conduits. Pour vous, la seule façon de sortir est de
grimper le long d'un de ces conduits de cheminée. Bien qu'il n'y
ait pas d'échelle, les aspérités du mur de pierre offrent de
nombreuses prises.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez sortir de la pièce où vous vous trouvez en montant par le conduit qui se trouve à votre gauche, rendez-vous au :"))
    st.page_link("tomes/tome5/page_162.py", label="162", icon="📄")

    st.write_stream(stream_text("Si vous préférez emprunter le conduit de droite, rendez-vous au :"))
    st.page_link("tomes/tome5/page_23.py", label="23", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
