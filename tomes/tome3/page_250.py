import streamlit as st
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

check_inventory(current_page_number=250, book=3)

fr_text = """
La fiole se fracasse entre vos mains et le liquide noir se répand
sur la table de pierre. Maudissant votre malchance, vous reniflez
prudemment quelques gouttes de la potion qui sont restées dans
un fragment de verre incurvé.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.caption("*Le Cimetière des Anciens se trouve dans une aventure précédente : répondez selon votre propre parcours.*")
    st.write_stream(stream_text("Si vous avez déjà eu l'occasion de traverser le Cimetière des Anciens, rendez-vous au :"))
    st.page_link("tomes/tome3/page_77.py", label="77", icon="📄")
    st.write_stream(
        stream_text(
            "Sinon, l'odeur âcre de ce liquide ne vous inspire guère confiance et vous vous débarrassez de la "
            "fiole brisée. Revenez ensuite au 10 pour faire un nouveau choix :"
        )
    )
    st.page_link("tomes/tome3/page_10.py", label="10", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
