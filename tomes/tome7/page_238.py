import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
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

check_inventory(current_page_number=238, book=7)

fr_text = """
Vous retournez le corps avec l'extrémité de votre botte et vous le
fouillez rapidement. Voici les objets que vous trouvez :

- 1 Hache
- 1 Épée
- 1 Poignard
- 2 Pièces d'Or

Prenez les objets que vous souhaitez garder avant de vous enfuir par l'escalier.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_button("HACHE", key="hache")
    pickup_button("ÉPÉE", key="epee")
    pickup_button("POIGNARD", key="poignard")
    pickup_gold(2, key="or")

    st.write_stream(stream_text("Rendez-vous alors au :"))
    st.page_link("tomes/tome7/page_55.py", label="55", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
