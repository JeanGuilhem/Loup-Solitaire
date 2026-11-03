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

check_inventory(current_page_number=127, book=4)

fr_text = """
Tandis que vous repoussez le corps de l'Élix qui vient de tomber
mort, une bataille désespérée continue de faire rage autour de
vous. Deux de vos hommes sont étendus sur le sol, la gorge
déchirée par les féroces créatures. Le cadavre d'un autre Elix
transpercé par une épée s'est effondré sur un troisième
patrouilleur qui reste coincé sous le monstre mort. Le quatrième
patrouilleur a atteint l'escalier et porte des coups désespérés à la
tête d'une des créatures qui lui a enfoncé les dents dans le pied.
Les Gardes ne donnent plus signe de vie. Ils ont été précipités au
fond du puits de mine dans les profondeurs d'une rivière
souterraine.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez porter secours au patrouilleur coincé sous le cadavre de l'Élix, rendez-vous au :"))
    st.page_link("tomes/tome4/page_178.py", label="178", icon="📄")

    st.write_stream(stream_text("Si vous préférez prêter main-forte à celui qui se bat au pied de l'escalier, rendez-vous au :"))
    st.page_link("tomes/tome4/page_245.py", label="245", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
