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

check_inventory(current_page_number=289, book=7)

fr_text = """
La lumière brille intensément dans l'obscurité du passage
humide. Ce dernier débouche bientôt dans une caverne haute et
voûtée d'où pendent de nombreux stalactites aux reflets nacrés,
ressemblant à de longues lances de pierre. Des ténèbres, vous
parviennent des bruits étranges qui vous donnent la chair de
poule. Prudemment, vous traversez la caverne, puis vous
continuez votre chemin à travers un dédale de tunnels sinueux.
Vous avancez péniblement en vous égratignant la tête à des
endroits trop bas et en glissant sur les pierres moussues du sol.
Vous parvenez enfin à une pièce aux murs lisses, creusée avec
précision dans le roc dur et noir. Sur votre gauche, un escalier
conduit à l'entrée d'un tunnel, et vous apercevez en face de vous
une grosse porte en pierre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez examiner cette porte en pierre, rendez-vous au :"))
    st.page_link("tomes/tome7/page_274.py", label="274", icon="📄")

    st.write_stream(stream_text("Si vous préférez monter l'escalier, rendez-vous au :"))
    st.page_link("tomes/tome7/page_193.py", label="193", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
