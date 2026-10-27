import streamlit as st
from inventory import (
    add_to_inventory,
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    is_new_page,
    show_illustrations,
)
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=10, book=2)

fr_text = """
Vous empochez le billet (inscrivez-le sur votre Feuille d'Aventure dans
la case d'Objets Spéciaux) et l'homme vous conduit à la diligence qui
attend à proximité de la porte Est du port. La diligence est vide et vous
vous asseyez près d'une des fenêtres de forme circulaire. Vous
constatez avec soulagement que le siège est très confortable ; c'est un
avantage que vous appréciez car il vous faudra voyager sept jours
durant pour atteindre Port Bax. Vous rangez votre équipement sous la
banquette, vous vous adossez confortablement et vous vous laissez
gagner par le sommeil. Lorsque vous vous éveillez, cinq autres
passagers ont pris place dans la diligence qui fait route en direction de
Durenor.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page() and not has_item("BILLET DE DILIGENCE"):
        add_to_inventory("BILLET DE DILIGENCE")
    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous tirez 0, 1, 2 ou 3, rendez-vous au 51. 4, 5 ou 6, rendez-vous au 195. 7, 8 ou 9, rendez-vous au 339."))
    number = hazard_roll()
    if number is not None and 0 <= number <= 3:
        st.page_link("tomes/tome2/page_51.py", label="51", icon="📄")
    elif number is not None and 4 <= number <= 6:
        st.page_link("tomes/tome2/page_195.py", label="195", icon="📄")
    elif number is not None and 7 <= number <= 9:
        st.page_link("tomes/tome2/page_339.py", label="339", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
