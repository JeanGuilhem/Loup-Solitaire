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

check_inventory(current_page_number=158, book=5)

fr_text = """
Vous entrez dans une galerie qui abrite une magnifique
mosaïque. Des milliers de minuscules fragments de perles et d'or
brillent dans le soleil couchant, irisant les hauts murs de marbre.
Un groupe de courtisans déambule dans la galerie et vous devez
vous dissimuler derrière un énorme pilier. Vous attendez que le
bruit de leurs pas s'éloigne avant de ressortir en pleine lumière.
Depuis longtemps, tout espoir de signer un traité de paix a
disparu et il ne vous reste plus maintenant qu'à vous enfuir du
Palais et à retourner au Sommerlund le plus vite possible d'une
manière ou d'une autre. Vous quittez rapidement la galerie en
suivant un couloir vers l'ouest et vous arrivez bientôt à un
croisement où le couloir tourne brusquement vers le nord.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome5/page_58.py", label="58", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
