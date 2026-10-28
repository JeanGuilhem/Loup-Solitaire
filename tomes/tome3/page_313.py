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

check_inventory(current_page_number=313, book=3)

fr_text = """
Les cadavres des mutants sont étendus à vos pieds. Vous vous
apprêtez à les enjamber pour attaquer la créature qui les
commande mais, à ce moment, plusieurs autres de ces
misérables monstres apparaissent aux côtés de leur maître. Ils
sont trop nombreux pour que vous ayez une chance de leur
résister et il vous faut donc vous enfuir au plus vite pour
échapper à une mort certaine. Vous vous précipitez donc vers la
porte par laquelle vous êtes entré et vous courez le long du
couloir principal aussi vite que vos jambes tremblantes peuvent
vous porter.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome3/page_130.py", label="130", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
