import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    is_new_page,
    remove_from_inventory,
    show_illustrations,
    show_map,
    spend_gold,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=232, book=6)

fr_text = """
L'aubergiste, un petit homme gras aux yeux porcins, vous
accueille avec un sourire forcé. Un torchon noir de crasse pend
au bout d'une corde attachée à son poignet. C'est avec ce bout de
chiffon qu'il essuie le comptoir en étalant un peu plus la saleté. «
Vous avez bien de la chance, mon ami, dit-il, en enfonçant la
main dans la poche de son tablier à rayures. Il nous reste une
chambre : la 17. (Il sort de son tablier une clé en fer qu'il pose sur
le comptoir.) On paie d'avance, ça fait 3 Pièces d'Or. » Vous
payez l'aubergiste (n'oubliez pas de rayer 3 Pièces d'Or sur votre
Feuille d'Aventure) et vous glissez la clé dans votre poche tout en
contemplant le soir qui tombe par la fenêtre ouverte. Mais
subitement, vous vous rappelez que vous n'avez pas mangé et
que vous avez besoin d'un bon Repas.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        st.session_state["visibility_chambre_232"] = "payée" if spend_gold(3) else "impayée"
    if st.session_state.get("visibility_chambre_232") == "payée":
        st.write("*Vous payez la chambre 17 : 3 Pièces d'Or.*")
    else:
        st.warning("Vous n'avez pas les 3 Pièces d'Or demandées par l'aubergiste.")

    st.write_stream(stream_text("Si vous souhaitez vous asseoir à une table pour commander un repas, rendez-vous au :"))
    st.page_link("tomes/tome6/page_328.py", label="328", icon="📄")

    st.write_stream(stream_text("Si vous préférez prendre un Repas de votre Sac à Dos et rester dans votre chambre, rendez-vous au :"))
    if st.button("Prendre un Repas du Sac à Dos (219)", disabled=not has_item("REPAS")):
        remove_from_inventory("REPAS")
        st.switch_page("tomes/tome6/page_219.py")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
