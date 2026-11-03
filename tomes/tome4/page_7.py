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

check_inventory(current_page_number=7, book=4)

fr_text = """
Votre adversaire tombe de selle, le pied coincé dans l'un des
étriers, et son corps est entraîné par le cheval qui part au galop.
Le vacarme de la bataille fait rage autour de vous. Vous vous
rendez compte alors que ces cavaliers en armure ne sont pas des
brigands ordinaires. Ils combattent en effet avec une discipline et
une habileté dont ne sont guère coutumiers les hors-la-loi du
Pays Sauvage. Un cheval passe à côté de vous, portant le cadavre
d'un patrouilleur encore en selle. Vous saisissez les rênes de
l'animal et vous récupérez une corne de guerre, accrochée au cou
de l'homme mort. Si vous voulez éviter un désastre complet, vous
savez en effet qu'il vous faut au plus vite sonner la retraite. Vous
tournez votre monture en direction du sud et vous lancez au
galop le cheval éclaboussé de sang. Les rescapés de votre troupe
vous suivent de près, tandis que résonnent à vos oreilles les cris
de victoire de l'ennemi.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome4/page_154.py", label="154", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
