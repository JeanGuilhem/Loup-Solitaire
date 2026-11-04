import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
    spend_gold,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=276, book=5)

fr_text = """
« Pourquoi me demandez-vous cela ? rétorque-t-elle d'une voix
soupçonneuse tout en clignant des yeux pour sécher ses larmes.
Quel genre d'affaires voulez-vous traiter avec le vieux Tipasa ? »
« C'est un ami », répond Banedon en posant une Pièce d'Or sur le
comptoir de la taverne. Aussitôt, la vieille femme recouvre la
pièce de sa main avec une expression de malice et de convoitise.
« Soushilla est vieille, sa mémoire n'est plus très bonne », dit-elle
en fixant du regard la bourse de Banedon. Celui-ci tire sur les
cordons pour sortir une autre pièce mais sa bourse a été vidée
par un habile pickpocket et elle ne contient plus la moindre pièce !
Banedon devient rouge comme une pivoine et, tout penaud,
évite votre regard narquois. « Cinq Pièces d'Or pourraient me
rafraîchir la mémoire », reprend la vieille en s'adressant à vous
cette fois-ci.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez lui donner les 5 Pièces d'Or qu'elle réclame, déduisez-les sur votre Feuille d'Aventure puis rendez-vous au :"))
    if st.button("Payer 5 Pièces d'Or", disabled=st.session_state.purse < 5):
        spend_gold(5)
        st.switch_page("tomes/tome5/page_326.py")

    st.write_stream(stream_text("Si vous n'avez pas les moyens de la payer ou si vous ne le souhaitez pas, quittez la taverne et rendez-vous au :"))
    st.page_link("tomes/tome5/page_202.py", label="202", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
