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

check_inventory(current_page_number=339, book=7)

fr_text = """
Des volutes de fumée commencent à s'élever des cadavres, et l'un
d'entre eux prend brusquement feu. Rapidement, vous sautez
par-dessus la dalle, loin des flammes et des vapeurs suffocantes.
Les autres corps, à leur tour, deviennent la proie des flammes qui
sifflent et crépitent comme un démon en furie. Vous continuez le
long du tunnel et vous apercevez le guerrier, assis sur ses talons,
les mains posées sur la garde de son épée. Un sourire parcourt
son visage mal rasé : « Vous êtes brave ! Je peux vous l'assurer,
j'connais personne à part vous qui puisse faire face à trois Dhax
affamés. » Il saute sur ses pieds, rengaine son épée et vous tend
la main en signe d'amitié.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_12.py", label="12", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
