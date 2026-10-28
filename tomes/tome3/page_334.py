import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=334, book=3)

fr_text = """
Un panneau s'ouvre à côté du pilier de droite, découvrant un
compartiment secret dans lequel a été dissimulée une
magnifique Pierre Rayonnante. Elle est tiède au toucher et ses
facettes étincellent. Si vous souhaitez conserver cette Pierre
Rayonnante, glissez-la dans votre poche et inscrivez-la sur votre
Feuille d'Aventure dans la case Objets Spéciaux.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if not has_item("PIERRE RAYONNANTE"):
        pickup_button("PIERRE RAYONNANTE", key="pierre", label="Prendre la Pierre Rayonnante")
    st.write_stream(stream_text("Si vous souhaitez appuyer à nouveau sur les boutons, rendez-vous au :"))
    st.page_link("tomes/tome3/page_65.py", label="65", icon="📄")
    st.write_stream(stream_text("Si vous préférez quitter le temple, rendez-vous au :"))
    st.page_link("tomes/tome3/page_306.py", label="306", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
