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

check_inventory(current_page_number=323, book=4)

fr_text = """
Vous lâchez la corde de votre arc ; la flèche siffle et vient
s'enfoncer profondément dans l'épaule du chef des brigands.
Vous l'entendez hurler de douleur mais, bien qu'il soit gravement
blessé, il tente malgré tout de rassembler ses hommes. Vous vous
penchez pour ramasser une autre flèche, mais vous constatez
avec horreur que le carquois du soldat mort est vide. Relevant la
tête, vous apercevez deux Guerriers vassagoniens qui ont mis
pied à terre et escaladent la barricade en se dirigeant vers vous.
Vous jetez votre arc et vous courez vers un grand tonneau d'eau
défendu par un robuste sergent du Sommerlund. Autour de lui,
le sol est jonché de cadavres ennemis. « Tirez sur le chef ! »
ordonnez-vous en montrant l'officier blessé. Le sergent vise et
tire aussitôt une flèche. Celle-ci décrit une courbe dans un ciel
envahi de fumée et transperce le plastron étincelant du chef des
brigands. Ses yeux cruels se brouillent et se ferment, puis il glisse
à bas de son cheval, la flèche plantée dans le cœur.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome4/page_148.py", label="148", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
