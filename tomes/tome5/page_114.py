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

check_inventory(current_page_number=114, book=5)

fr_text = """
Le conduit de la cheminée s'incline de plus en plus pour devenir
totalement horizontal et il mène désormais vers le sud. Bien que
la chaleur soit accablante, la vapeur s'est dissipée. Votre corps est
devenu extrêmement sensible et vous progressez avec beaucoup
de difficultés le long du boyau. Tout espoir concernant la
signature du traité de paix avec le nouveau Zakhan s'est évanoui.
Il ne vous reste plus maintenant qu'à essayer de sortir de cet
égout d'enfer et trouver un moyen quelconque afin de retourner
au Sommerlund le plus vite possible. Mais soudain vous
apercevez, à quelques mètres, une grille d'aération de forme
carrée. La plaque est très rouillée et vous devez vous allonger sur
le dos et la soulever avec vos deux pieds pour la déplacer. Cet
effort violent épuise vos dernières forces mais vous parvenez à
vos fins. De plus, par un hasard extraordinaire, vous vous
retrouvez dans le bâtiment de Barrakeesh que vous aviez le plus
besoin de visiter : les Bains Publics. Un séjour dans cet
établissement s'avère en effet indispensable !
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_90.py", label="90", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
