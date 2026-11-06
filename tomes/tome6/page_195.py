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

check_inventory(current_page_number=195, book=6)

fr_text = """
Soudain, vous sentez qu'un grave danger vous menace et vous
collez votre oreille contre le trou de la serrure pour essayer de
comprendre ce que dit le prédicateur : «... et je vous en conjure,
mes frères, n'écoutez pas les théories obscures et pernicieuses de
Gwynian. L'étoile qui brillait cette nuit était un signe
d'avertissement : nous devons protéger notre savoir et garder
jalousement le secret de la Pierre de la Sagesse. Nous devons
arrêter tous ceux qui voudraient s'en emparer pour utiliser son
pouvoir à des fins malfaisantes !» A la fin du discours,
l'assemblée reprend en chœur: «Gardons le secret, gardons le
secret, gardons le secret... » Mais, tout à coup, vous entendez le
cliquetis d'une clé dans la serrure et vous courez rapidement
vous cacher dans l'encadrement d'une porte. La réunion s'achève
et la congrégation s'apprête à quitter les lieux. Les hommes vêtus
de grands habits marron quittent le temple puis se dispersent,
mais un petit groupe se dirige vers votre cachette. Si vous restez
là, vous allez sûrement être découvert ! Sans une seconde
d'hésitation, vous poussez la porte et entrez.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_127.py", label="127", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
