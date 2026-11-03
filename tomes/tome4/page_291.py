import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=291, book=4)

fr_text = """
Le passage mène à une porte cloutée de fer. Collant votre oreille
contre le panneau de bois brut, vous percevez des voix de l'autre
côté.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous maîtrisez la Discipline Kaï du Camouflage, rendez-vous au :'))
    if has_kai('Le Camouflage'):
        st.page_link("tomes/tome4/page_172.py", label="172", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome4/page_172.py", label="172", icon="📄", disabled=True)
    st.write_stream(stream_text('Sinon, vous pouvez dégainer votre arme, ouvrir la porte et vous rendre au :'))
    st.page_link("tomes/tome4/page_93.py", label="93", icon="📄", disabled=has_kai("Le Camouflage"))
    st.write_stream(stream_text("Vous avez également la possibilité de revenir sur vos pas dans la galerie pour suivre la voie ferrée dans le tunnel orienté à l'ouest. Rendez-vous dans ce cas au :"))
    st.page_link("tomes/tome4/page_55.py", label="55", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
