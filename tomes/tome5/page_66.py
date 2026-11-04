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

check_inventory(current_page_number=66, book=5)

fr_text = """
Une sentinelle d'aspect cruel, armée d'un long fouet, monte la
garde devant le grand porche des cuisines. Le Garde passe son
temps à malmener les esclaves qui vont et viennent autour de lui,
les frappant de son fouet tout en les houspillant méchamment.
Vous jugez qu'il serait bien trop risqué de vous attaquer à lui et
vous dirigez maintenant votre attention sur les fenêtres des
cuisines. Le Garde est à présent en train de battre un malheureux
esclave qui vient de renverser un panier de fruits, et il vous est
donc possible de traverser les jardins en courant sans vous faire
remarquer et de vous glisser dans l'encadrement d'une haute
fenêtre en ogive qui donne sur les cuisines. Là, à votre grande
consternation, vous observez qu'il y a deux Gardes assis à
l'intérieur, juste au-dessous du rebord de la fenêtre où vous vous
trouvez. Il suffit qu'ils tournent la tête pour vous apercevoir...
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous désirez sauter dans les jardins en contrebas et tenter de pénétrer dans le Palais en passant par la chambre des Trophées du Zakhan, rendez-vous au :"))
    st.page_link("tomes/tome5/page_149.py", label="149", icon="📄")

    st.write_stream(stream_text("Si vous préférez attaquer les deux Gardes par surprise, avant qu'ils ne vous repèrent, rendez-vous au :"))
    st.page_link("tomes/tome5/page_124.py", label="124", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
