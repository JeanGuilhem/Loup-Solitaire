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

check_inventory(current_page_number=319, book=3)

fr_text = """
Vous visez soigneusement et vous jetez les Pièces d'Or dans le
couloir. Alerté par ce bruit soudain, le guerrier tire son épée en
os et va voir de quoi il retourne. Votre plan s'est révélé efficace :
le Barbare est en effet à quatre pattes, en train de chercher les
Pièces et il ne vous voit pas passer derrière lui. Vous pouvez à
présent monter l'escalier.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.caption("*Les Pièces d'Or que vous avez lancées ont déjà été retirées de votre bourse.*")
    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome3/page_332.py", label="332", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
