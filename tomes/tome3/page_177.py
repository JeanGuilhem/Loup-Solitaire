import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=177, book=3)

fr_text = """
Vous reconnaissez aussitôt l'odeur âcre de Ronces des Cimetières
distillées. Cette décoction de couleur noire est un poison puissant
et vous rebouchez aussitôt la fiole pour empêcher les vapeurs
nocives de s'en échapper. Si vous souhaitez conserver cette
Potion, inscrivez-la sur votre Feuille d'Aventure dans la case des
objets contenus dans votre Sac à Dos.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if not has_item("POTION DE RONCES DES CIMETIÈRES"):
        pickup_button(
            "POTION DE RONCES DES CIMETIÈRES", key="potion_noire", label="Conserver la Potion de Ronces des Cimetières"
        )
    st.write_stream(stream_text('Retournez à présent au 10 pour faire un nouveau choix :'))
    st.page_link("tomes/tome3/page_10.py", label="10", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
