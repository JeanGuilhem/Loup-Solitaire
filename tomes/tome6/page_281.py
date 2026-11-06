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

check_inventory(current_page_number=281, book=6)

fr_text = """
« Mes plus humbles remerciements, dit le frêle vieillard après que
vous l'avez relevé. Je vous en serai toujours reconnaissant. »
Vous l'escortez jusqu'à sa table en le soutenant par le bras. Il
rassemble rapidement ses affaires et se présente : « Mon nom est
Cyrilus. Je suis magicien, dit-il, d'une voix pleine d'humilité
comme pour s'excuser d'un défaut ou d'une faiblesse. Je ne
prétends pas connaître toutes les arcanes de la magie - mes
talents sont plus modestes, et je me contente de quelques tours
très simples. Je gagne ma vie en faisant des tours de passe-passe
et d'escamotage pour divertir les courtisans de Varetta. » En
entendant le mot «Varetta», votre regard change brusquement
d'expression et Cyrilus s'en aperçoit immédiatement.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez l'interroger sur la Pierre de la Sagesse de Varetta, rendez-vous au :"))
    st.page_link("tomes/tome6/page_83.py", label="83", icon="📄")

    st.write_stream(stream_text("Si vous ne voulez pas le questionner, souhaitez-lui une bonne nuit et rendez-vous au :"))
    st.page_link("tomes/tome6/page_239.py", label="239", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
