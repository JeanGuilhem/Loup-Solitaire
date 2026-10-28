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

check_inventory(current_page_number=324, book=3)

fr_text = """
Tandis que le répugnant Akranionor meurt à vos pieds, vous
voyez le traître bossu descendre de sa plate-forme et se précipiter
vers une porte, un peu plus loin. Vous vous apprêtez à le
poursuivre lorsque vous vous immobilisez soudain en découvrant
le corps de Loi-Kymar étendu dans le fossé. Il est mort, tué au
cours du combat psychique qui l'a opposé à Vonotar. La colère
bouillonne en vous et vous brandissez votre arme en vous
lançant à la poursuite de l'infâme renégat ; cette fois, vous êtes
décidé à le tuer. La porte s'ouvre sur un long couloir au bout
duquel se trouve une arcade fermée par des rideaux. D'un geste
vif, vous écartez les rideaux et vous continuez à courir.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome3/page_61.py", label="61", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
