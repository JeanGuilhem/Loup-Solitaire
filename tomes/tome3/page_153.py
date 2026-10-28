import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies, ls_death

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=153, book=3)

fr_text = """
Vous avez presque réussi à traverser le lac lorsqu'une catastrophe
survient. Votre pied droit, en effet, passe à travers la glace et vous
êtes coincé à hauteur du genou. Vous essayez désespérément de
vous libérer, mais il n'y a rien à faire, vous êtes pris au piège.
Quelques secondes plus tard, la couche de glace qui recouvre le
lac se fracasse dans un terrible craquement : le monstre des
profondeurs dont vous aviez auparavant aperçu la silhouette
vient ainsi de faire son apparition à la surface. Paralysé
d'horreur, vous voyez alors la gueule noire et visqueuse de la
créature s'ouvrir pour exhiber deux rangées de dents tranchantes
comme des rasoirs. Le monstre venu du fond des âges se
précipite sur vous et cette gueule béante sera la dernière vision
que vous emporterez de ce monde, avant que la bête ne vous
avale. Votre mission s'achève ici en même temps que votre vie.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    show_illustrations()
    ls_death()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
