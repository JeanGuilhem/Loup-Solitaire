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

check_inventory(current_page_number=326, book=4)

fr_text = """
Vous comprenez soudain que vous venez d'entrer dans un
lointain secteur des mines de Maaken, en passant par une galerie
désaffectée creusée dans les contreforts des montagnes. Pendant
des centaines d'années, les filons qui abondent dans les
profondeurs de la chaîne de Maaken ont représenté tout à la fois
une bénédiction et un fléau pour des milliers d'hommes venus ici
chercher fortune. Des prospecteurs y ont trouvé parfois des
richesses qui dépassaient leurs espérances les plus insensées,
tandis que d'autres ont péri sans laisser de traces dans un
labyrinthe de souterrains glacés et humides. Si vous parveniez à
rejoindre une partie de la mine encore en exploitation, vous
pourriez atteindre Ruanon à travers son réseau de tunnels.
Ruanon se trouvant au sud, vous décidez par conséquent
d'emprunter le souterrain orienté au sud.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome4/page_101.py", label="101", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
