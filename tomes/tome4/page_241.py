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

check_inventory(current_page_number=241, book=4)

fr_text = """
Le plafond de la grotte est si bas que vous êtes contraints de vous
accroupir au fond du bateau pour éviter de vous cogner la tête.
Pendant presque une heure, l'embarcation est emportée dans un
labyrinthe de cours d'eau souterrains. Soudain, le bateau
s'immobilise. Vous vous êtes échoués sur une rive de galets, dans
un tunnel beaucoup plus haut que tous ceux traversés jusqu'à
présent. Au sud, la rivière continue, s'enfonçant dans une paroi
rocheuse à travers une arcade ; à l'est vous apercevez une autre
rive de galets ainsi qu'un nouveau tunnel, mais au sol ferme cette
fois-ci.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez ramer en direction de cette autre rive, puis abandonner le bateau et continuer à pied le long du tunnel, rendez-vous au :'))
    st.page_link("tomes/tome4/page_309.py", label="309", icon="📄")

    st.write_stream(stream_text('Si vous préférez poursuivre votre chemin le long de la rivière, rendez-vous au :'))
    st.page_link("tomes/tome4/page_115.py", label="115", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
