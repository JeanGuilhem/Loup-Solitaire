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

check_inventory(current_page_number=157, book=7)

fr_text = """
Vous sortez rapidement une Graine de Feu de votre poche et
vous la lancez de toutes vos forces sur le socle. Le bloc de marbre
éclate dans un craquement sonore, puis disparaît dans les
flammes. La main prend feu à son tour ; vous la voyez se tordre et
se crisper spasmodiquement tandis que les flammes dévorent la
peau squameuse. Bientôt, une infecte odeur de chair brûlée
accompagnée d'une fumée noire envahit la pièce.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        remove_from_inventory("GRAINE DE FEU")
    st.caption("Vous rayez une Graine de Feu de votre Feuille d'Aventure.")

    st.write_stream(stream_text("Si vous voulez vous reculer un peu et attendre que les flammes s'éteignent, rendez-vous au :"))
    st.page_link("tomes/tome7/page_128.py", label="128", icon="📄")

    st.write_stream(stream_text("Si vous préférez contourner le feu sans plus attendre et vous engager dans le passage qui s'ouvre au-delà, rendez-vous au :"))
    st.page_link("tomes/tome7/page_284.py", label="284", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
