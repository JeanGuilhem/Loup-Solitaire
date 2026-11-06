import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    receive_gold,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=91, book=6)

fr_text = """
Votre attention est attirée par une table au centre de la salle,
où six hommes rubiconds sont en train de jouer aux cartes. Ils
jouent contre un croupier qui distribue les cartes une par une.
Vous ne tardez pas à remarquer que le jeu dont il se sert est
truqué... Dès qu'un joueur abandonne la partie, vous prenez sa
place. Inutile de dire que vous gagnez aisément le premier tour,
puis les suivants, puisque vous savez comment le jeu a été
truqué.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard et ajoutez 5 au chiffre que vous avez tiré. Le résultat obtenu indique le nombre de Pièces d'Or que vous remportez avant que le donneur, soupçonnant votre manœuvre, indique la fin de la partie."))
    roll = hazard_roll()
    if roll is not None:
        receive_gold(roll + 5, key="t6_91_gain")

    st.write_stream(stream_text("Maintenant que vous avez de nouveau de l'argent en poche, vous pouvez approcher du comptoir et demander une chambre pour la nuit, rendez-vous dans ce cas au :"))
    st.page_link("tomes/tome6/page_232.py", label="232", icon="📄")

    st.write_stream(stream_text("Si vous préférez aller vous attabler et commander un repas, rendez-vous au :"))
    st.page_link("tomes/tome6/page_172.py", label="172", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
