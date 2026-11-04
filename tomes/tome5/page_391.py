import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    kai_rank,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=391, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Tandis que vous vous enfoncez dans l'Arboretum, des
croassements aigus retentissent au-dessus du plafond de verdure
que forment les plantes grimpantes et les branches basses des
arbres. L'air est humide comme en pleine jungle. Vous essayez
d'avancer le plus vite possible, mais votre progression est difficile
car la couche d'humus qui recouvre le sol est molle et collante
comme de la vase. Soudain, un léger bruit, à quelques mètres de
vous, vous met en alerte. D'un bond, vous plongez dans les
broussailles pour vous dissimuler au moment même où une
poignée de Drakkars, menés par un personnage vêtu de rouge,
arrivent dans votre direction.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez le titre de Guerrier Kaï, ou un titre supérieur, rendez-vous au :"))
    if kai_rank() >= 8:
        st.page_link("tomes/tome5/page_242.py", label="242", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_242.py", label="242", icon="📄", disabled=True)
    st.write_stream(stream_text("Si vous ne possédez pas cette distinction Kaï, rendez-vous au :"))
    if kai_rank() >= 8:
        st.page_link("tomes/tome5/page_222.py", label="222", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome5/page_222.py", label="222", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
