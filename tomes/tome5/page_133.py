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

check_inventory(current_page_number=133, book=5)

fr_text = """
Vous reconnaissez les empreintes de Kwaraz dans la boue
visqueuse du trottoir. Les Kwaraz sont de gigantesques reptiles
carnivores et la taille très variée des empreintes signifie que le
tunnel abrite sûrement toute une colonie de ces répugnantes
créatures. Vous jugez qu'il serait bien trop dangereux de
poursuivre dans cette direction, et vous préférez grimper les
marches d'un escalier étroit qui mène à une pièce située au-dessus
du tunnel. L'air au moins y est sec, bien que les gaz
méphitiques se répandent partout. Vous suivez un étroit passage
tout d'abord vers l'ouest, puis vers le sud mais votre cœur se
serre lorsque vous distinguez dans l'obscurité un mur qui bouche
le tunnel.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous désirez chercher une issue cachée, rendez-vous au :"))
    st.page_link("tomes/tome5/page_33.py", label="33", icon="📄")

    st.write_stream(stream_text("Si vous préférez faire demi-tour et redescendre vers le trottoir, rendez-vous au :"))
    st.page_link("tomes/tome5/page_64.py", label="64", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
