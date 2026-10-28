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

check_inventory(current_page_number=130, book=3)

fr_text = """
Vous revenez sur vos pas en courant, vous arrivez au croisement
et vous prenez le couloir orienté à l'est. Un Barbare des Glaces
vous bloque le passage, mais vous vous ruez sur lui. D'un violent
coup d'épaule qui vous ébranle de la tête aux pieds, vous le
repoussez contre le mur et vous continuez à courir jusqu'à un
escalier dont vous montez les marches quatre à quatre. Vous êtes
parvenu à mi-hauteur lorsque vous entendez les hurlements
sinistres de vos monstrueux poursuivants. Au sommet de
l'escalier, vous découvrez un couloir orienté nord-sud.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez prendre la direction du nord, rendez-vous au :"))
    st.page_link("tomes/tome3/page_198.py", label="198", icon="📄")
    st.write_stream(stream_text("Si vous préférez aller au sud, rendez-vous au :"))
    st.page_link("tomes/tome3/page_69.py", label="69", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
