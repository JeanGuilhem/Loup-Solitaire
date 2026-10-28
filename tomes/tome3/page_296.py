import streamlit as st
from combat import combat
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

check_inventory(current_page_number=296, book=3)

fr_text = """
Malheureusement, les gardes se doutent de quelque chose et ils
vous interpellent dans leur étrange langage. Il ne vous reste plus
à présent qu'à les attaquer avant qu'ils aient le temps de donner
l'alerte. Les vapeurs du mélange d'herbes affectent cependant vos
adversaires et le combat en sera ainsi facilité. Vous n'aurez en
effet à livrer que 3 Assauts ; à la fin du troisième Assaut, les
Barbares des Glaces s'écrouleront à vos pieds, endormis par la
mixture fumante.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("BARBARES DES GLACES", 17, 30)], max_rounds=3)
    if outcome in ("win", "rounds_over"):
        if outcome == "rounds_over":
            st.write_stream(stream_text("À la fin du troisième Assaut, les Barbares des Glaces s'écroulent à vos pieds, endormis par la mixture fumante."))
        st.write_stream(stream_text(
            "Vous faites signe à Loi-Kymar de s'approcher. A votre grande joie, vous constatez alors que l'une des "
            "magnifiques portes incrustées de pierreries n'est pas fermée à clé. Vous l'entrebâillez doucement et vous "
            "entrez dans la salle du Trône du Brumalmarc, repaire de Vonotar le Traître. Rendez-vous au :"
        ))
        st.page_link("tomes/tome3/page_173.py", label="173", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
