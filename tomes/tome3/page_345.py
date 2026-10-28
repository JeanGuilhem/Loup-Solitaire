import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    remove_from_inventory,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=345, book=3)

fr_text = """
Vous fermez les yeux et vous vous concentrez pour essayer de
résister à la Force Mentale. Peu à peu, vous parvenez à
surmonter votre douleur, juste assez longtemps pour pouvoir
arracher le Bracelet de votre poignet et le jeter sur le sol.
Maudissant votre malchance, vous poursuivez alors votre chemin
d'un pas chancelant en vous dirigeant vers le croisement situé à
l'extrémité du couloir.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        remove_from_inventory("BRACELET D'OR")
    st.caption("*Le Bracelet d'Or a été retiré de vos Objets Spéciaux.*")
    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome3/page_215.py", label="215", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
