import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=39, book=3)

fr_text = """
Jusqu'à présent, tout va bien. Les gardes ne semblent pas vous
prêter la moindre attention. Vous faites semblant de renouer les
lacets de vos bottes et vous cachez la coupe derrière un pilastre.
Vous retournez alors dans la cuisine et vous attendez que les
vapeurs fassent leur effet. Moins d'une minute plus tard, les
gardes s'écroulent sur le sol et vous pouvez vous approcher sans
encombre de la salle du Trône. Vous êtes enchanté de découvrir
que l'une des magnifiques portes incrustées de pierreries n'est
pas fermée à clé. Vous préparant à passer à l'attaque, vous
entrebâillez doucement la porte et vous entrez dans le repaire de
Vonotar.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome3/page_173.py", label="173", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
