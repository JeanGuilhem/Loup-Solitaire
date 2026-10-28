import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies, hazard_roll, handle_repas

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=155, book=3)

fr_text = """
Le vent glacé de la montagne a tôt fait de dissiper les brumes de
l'aube. Epuisé, transi jusqu'à la moelle et encore sous le choc des
récents événements, vous escaladez l'impitoyable paroi de roc
jusqu'à ce que vous parveniez enfin sur une large corniche où
vous vous sentez plus en sécurité. Vous êtes affamé, et il vous
faut prendre un Repas avant de continuer, sinon, vous perdrez 3
points d'ENDURANCE. N'oubliez pas de rayer ce Repas de votre
Feuille d'Aventure. La corniche en rejoint une autre que vous
avez beaucoup de mal à parcourir. Lorsque, enfin, vous arrivez
au bout, vous vous trouvez au sommet d'une paroi
impressionnante. Pour descendre dans l'étroit défilé que vous
apercevez à 300 mètres au-dessous, il vous faudra emprunter un
escalier particulièrement raide et dangereux dont les marches
sont taillées dans la glace.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    handle_repas()

    st.write_stream(
        stream_text(
            "Utilisez la Table de Hasard pour obtenir un chiffre. Si votre total d'ENDURANCE actuel est inférieur "
            "à 10, vous ôterez 2 au chiffre obtenu. Si ce total est supérieur à 20, vous ajouterez 1 au chiffre "
            "donné par la Table."
        )
    )
    roll = hazard_roll()
    if roll is not None:
        value = roll
        if st.session_state.endurance < 10:
            value -= 2
            st.write(f"*ENDURANCE inférieure à 10 : -2, total {value}.*")
        elif st.session_state.endurance > 20:
            value += 1
            st.write(f"*ENDURANCE supérieure à 20 : +1, total {value}.*")
        if value <= 2:
            st.write_stream(stream_text("Si le total obtenu se situe entre -2 et 2, rendez-vous au :"))
            st.page_link("tomes/tome3/page_248.py", label="248", icon="📄")
        else:
            st.write_stream(stream_text("S'il est de 3 à 10, rendez-vous au :"))
            st.page_link("tomes/tome3/page_191.py", label="191", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
