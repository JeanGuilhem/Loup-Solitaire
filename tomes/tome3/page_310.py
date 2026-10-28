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

check_inventory(current_page_number=310, book=3)

fr_text = """
Vous ouvrez la Sphère de Feu et, aussitôt, un mugissement
sonore retentit à vos oreilles. Le cyclone s'immobilise et il ne
s'approchera plus de vous tant que vous tiendrez dans vos mains
la Sphère enflammée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez quitter le temple, rendez-vous au :"))
    st.page_link("tomes/tome3/page_306.py", label="306", icon="📄")
    st.write_stream(stream_text("Si vous préférez examiner l'autel et l'alcôve qui l'abrite, rendez-vous au :"))
    st.page_link("tomes/tome3/page_72.py", label="72", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
