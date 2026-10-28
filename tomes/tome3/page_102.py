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

check_inventory(current_page_number=102, book=3)

fr_text = """
Un petit panneau à la base du pilier de gauche vient de coulisser,
révélant un compartiment secret. A l'intérieur, vous découvrez
une petite statuette : il s'agit d'une Effigie de pierre qui
représente une étrange créature dotée de tentacules.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez conserver cette Effigie, glissez-la dans votre poche : elle est rangée dans vos Objets Spéciaux."))
    if not has_item("EFFIGIE"):
        pickup_button("EFFIGIE", key="effigie", label="Prendre l'Effigie")
    st.write_stream(stream_text("Si vous souhaitez essayer à nouveau d'appuyer sur les boutons, rendez-vous au :"))
    st.page_link("tomes/tome3/page_65.py", label="65", icon="📄")
    st.write_stream(stream_text("Si vous préférez quitter le temple, rendez-vous au :"))
    st.page_link("tomes/tome3/page_306.py", label="306", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
