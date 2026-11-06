import streamlit as st
from inventory import (
    add_to_inventory,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
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

check_inventory(current_page_number=139, book=6)

fr_text = """
Vous soulevez la visière du casque de l'homme que vous venez
d'abattre, vous attendant à voir les traits grossiers d'un
quelconque bandit de grand chemin. Mais à votre grande stupeur,
vous découvrez le visage d'une femme, dont les yeux voilés par
la mort vous regardent fixement. Les formes de son corps sont
dissimulées par les épaisses plaques de son armure, et un
foulard placé devant sa bouche servait à déguiser le timbre de
sa voix. Vous trouvez peu d'indices pour l'identifier : une
hache, une bourse contenant 11 Pièces d'Or, un poignard et une
Broche en Argent, voilà tout, les tueurs à gages voyageant
léger. Après avoir examiné la Broche d'Argent de plus près, vous
décidez de la garder. (Inscrivez-la dans la case Objets Spéciaux
de votre Feuille d'Aventure.) Le visage de cette femme vous
semble quelque peu familier, mais vous n'arrivez pas à savoir
pourquoi... Laissant là cette énigme, vous reportez vos pensées
sur votre compagnon - sa vie est en danger ! Vous remontez en
selle et vous partez au triple galop sur le Pont de Denka pour
vous lancer à la poursuite des ravisseurs.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        add_to_inventory("BROCHE EN ARGENT")
    st.success("La Broche en Argent a été ajoutée à vos Objets Spéciaux.")
    pickup_gold(11, key="bourse")
    pickup_button("HACHE", key="hache", label="Prendre la Hache")
    pickup_button("POIGNARD", key="poignard", label="Prendre le Poignard")

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome6/page_39.py", label="39", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
