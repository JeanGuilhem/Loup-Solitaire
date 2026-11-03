import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, handle_repas, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=19, book=4)

fr_text = """
Vous reconnaissez aussitôt ces amulettes. Elles sont le symbole
du « Saint Ordre des Rédempteurs », une communauté de
pèlerins contemplatifs dont la vie est consacrée à la prière et à la
guérison. Vous présentez vos excuses pour avoir réagi d'une
manière trop hâtive et les deux hommes hochent leur tête rasée
en signe de pardon. Vos soldats ont établi le campement à l'abri
du dôme de marbre et tout le monde se prépare à une bonne nuit
de sommeil. Vous avez faim à présent et il vous faut prendre un
Repas sinon vous perdrez 3 points d'ENDURANCE.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    handle_repas()

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome4/page_233.py", label="233", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
