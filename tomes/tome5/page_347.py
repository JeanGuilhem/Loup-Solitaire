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

check_inventory(current_page_number=347, book=5)

fr_text = """
Tout en hurlant de douleur, vous tirez sur les rênes pour obliger
l'Itikar à prendre de l'altitude. Le guerrier Drakkar se trouve à
présent à plus de trente mètres au-dessus de vous, mais il est en
train d'effectuer un demi-tour afin de passer de nouveau à
l'attaque. Vous virez au sud pour éviter d'être pris entre deux
formations de Kraans qui convergent vers vous. Votre brusque
changement de direction augmente la distance qui vous sépare
de vos poursuivants, mais votre monture emplumée est
grièvement blessée et vous perdez pratiquement tout espoir de
vous en sortir. L'Itikar perd en effet tellement de sang qu'il peut
sombrer dans l'inconscience d'un moment à l'autre en vous
laissant choir comme une pierre vers le lac Inrahim. Soudain,
vous apercevez quelque chose dans le lointain; quelque chose qui
vous fait croire à nouveau aux miracles...
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome5/page_221.py", label="221", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
