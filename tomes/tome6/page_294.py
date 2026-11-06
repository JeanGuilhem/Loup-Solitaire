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

check_inventory(current_page_number=294, book=6)

fr_text = """
Tout à coup, vous apercevez les squelettes dessinés sur leurs
manteaux, et cela ranime en vous un souvenir qui vous fait frémir.
Ils sont habillés de la même façon que les prêtres malfaisants qui
accompagnaient le Seigneur de la Guerre, le traître Barraka, dans
le temple enfoui de Maaken. Ces hommes sont des disciples de
Vashna. Après la défaite de Barraka, ils s'enfuirent dans le sud
pour échapper à l'armée du Sommerlund. On pensait communément,
dans les régions des Fins de Terre, que leur confrérie avait été
détruite et leur pouvoir anéanti à tout jamais, mais cette
rencontre prouve qu'il n'en est rien. S'ils découvrent votre
véritable identité, ils mettront tout en œuvre pour vous détruire.
Leur chef, agacé, répète sa question et attend votre réponse avec
impatience.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez répondre « croyant », rendez-vous au :"))
    st.page_link("tomes/tome6/page_108.py", label="108", icon="📄")

    st.write_stream(stream_text("Si vous préférez répondre « non-croyant », rendez-vous au :"))
    st.page_link("tomes/tome6/page_67.py", label="67", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
