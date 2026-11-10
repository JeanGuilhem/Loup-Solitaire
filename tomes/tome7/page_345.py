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

check_inventory(current_page_number=345, book=7)

fr_text = """
Le guerrier n'essaie pas de parer votre attaque et reste la garde
baissée. Votre coup déchire profondément sa poitrine, et il vous
regarde, incrédule, en portant la main à sa blessure. Puis il
tombe lourdement sur les genoux et s'écrie d'une voix rauque : «
Pourquoi ? » tandis que ses paupières battent avant de se fermer
définitivement. Les créatures poussent des hurlements de joie
hystériques en voyant le guerrier tomber dans l'abîme enfumé,
puis elles s'avancent vers vous à longues enjambées.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez rester sur place pour affronter ces créatures, rendez-vous au :"))
    st.page_link("tomes/tome7/page_249.py", label="249", icon="📄")
    st.write_stream(stream_text("Si vous voulez les fuir en courant vers l'entrée du tunnel opposé, rendez-vous au :"))
    st.page_link("tomes/tome7/page_241.py", label="241", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
