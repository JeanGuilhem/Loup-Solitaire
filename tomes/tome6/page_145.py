import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    pickup_gold,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=145, book=6)

fr_text = """
Les survivants s'enfuient dans la nuit, abandonnant leur maître
et la moitié de leurs condisciples sur le pavé. Mettant pied à
terre, vous coupez la bourse qui pend à la ceinture du chef.
Elle contient 12 Pièces d'Or et une Bague en Rubis. Vous pouvez
garder l'argent et ce bijou si vous le souhaitez. Dans ce cas,
inscrivez la Bague en Rubis dans la case Objets Spéciaux de
votre Feuille d'Aventure, puis rangez-la dans votre poche.
Soudain, vous entendez un martèlement de bottes sur le pavé et
vous voyez surgir une troupe de soldats se frayant
dédaigneusement un passage parmi la foule des badauds attirés
par le spectacle. Sans perdre une seconde, vous rengainez votre
arme et vous remontez en selle, puis vous vous éloignez
discrètement dans l'obscurité de la rue.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_gold(12, key="bourse")
    pickup_button("BAGUE EN RUBIS", key="bague", label="Prendre la Bague en Rubis")

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_289.py", label="289", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
