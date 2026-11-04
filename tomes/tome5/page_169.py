import streamlit as st
from inventory import (
    buy_button,
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

check_inventory(current_page_number=169, book=5)

fr_text = """
Vous débouchez sur une large rue où des vendeurs se battent
pour un morceau de trottoir afin d'installer leurs tréteaux. La
foule se presse au marché ; chacun porte un brassard noir en
signe de deuil mais ici, contrairement au reste de Barrakeesh, les
affaires continuent normalement. Vous passez devant une
charrette remplie de brassards noirs au prix de 2 Pièces d'Or
l'unité.
"""

fr_text_2 = """
Vous vous éloignez rapidement de la charrette et vous
disparaissez dans une étroite ruelle bordée de nombreuses
tavernes et auberges. L'air est rempli d'odeurs de cuisine et de
vin aigre, et tout le passage résonne des cris et des bavardages de
la population. Votre attention est attirée par une affiche
placardée récemment sur le mur d'une taverne. Vous lisez la
première ligne écrite en gros caractères: LE ZAKHAN EST
MORT - VIVE LE ZAKHAN !
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez en acheter un, payez le vendeur et inscrivez votre nouvelle acquisition sur votre Feuille d'Aventure dans la case des Objets Spéciaux. Placez ce brassard autour du bras."))
    buy_button("BRASSARD NOIR", 2, key="brassard", label="Acheter un Brassard noir (2 Couronnes)")

    st.write(fr_text_2)

    st.write_stream(stream_text("Si vous souhaitez poursuivre la lecture de l'affiche, rendez-vous au :"))
    st.page_link("tomes/tome5/page_88.py", label="88", icon="📄")

    st.write_stream(stream_text('Si vous préférez continuer à avancer dans la ruelle, rendez-vous au :'))
    st.page_link("tomes/tome5/page_113.py", label="113", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
