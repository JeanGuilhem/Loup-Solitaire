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

check_inventory(current_page_number=183, book=7)

fr_text = """
La dalle reste immobile, quelle que soit la force avec laquelle
vous tapez mais, ce faisant, vous découvrez quelque chose qui se
trouvait auparavant caché sous la couche de poussière. Vous
grattez avec précaution le reste de saleté et vous apercevez,
profondément gravé dans le marbre gris, le dessin d'un serpent
enroulé sur lui-même. Au milieu est inscrit le nombre 123. Notez
ce nombre dans la marge de votre Feuille d'Aventure, il pourra
vous être utile plus tard au cours de votre aventure.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.info("Nombre à noter dans la marge de votre Feuille d'Aventure : **123**.")

    st.write_stream(stream_text("A présent, si vous souhaitez pénétrer dans le tunnel en sautant par-dessus la dalle, rendez-vous au :"))
    st.page_link("tomes/tome7/page_127.py", label="127", icon="📄")

    st.write_stream(stream_text("Si vous préférez entrer dans le tunnel en marchant sur la dalle, rendez-vous au :"))
    st.page_link("tomes/tome7/page_277.py", label="277", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
