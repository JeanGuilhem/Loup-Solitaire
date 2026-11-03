import streamlit as st
from combat import combat
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

check_inventory(current_page_number=287, book=4)

fr_text = """
A peine avez-vous fait une dizaine de pas, que la vieille femme se
laisse tomber sur le sol. « Une embuscade ! » s'écrie aussitôt l'un
des patrouilleurs. C'est le dernier mot qu'il prononcera jamais.
Un disque de métal aux bords acérés, jeté d'un balcon, vient en
effet de s'enfoncer profondément dans sa poitrine. Soudain, la
taverne est envahie de brigands qui font irruption par les portes
et les fenêtres. Poussant des cris de guerre aux accents barbares,
trois brigands se précipitent sur vous. Vous dégainez votre arme
et vous frappez, tranchant d'un seul coup la tête de deux des
brigands à la peau sombre. Le troisième est sur vous avant même
que les corps de ses camarades se soient effondrés sur le sol. Il
vous faut combattre ce Guerrier Pillard.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("GUERRIER PILLARD", 17, 27)])
    if outcome == "win":
        st.write_stream(stream_text('Si vous remportez la victoire, rendez-vous au :'))
        st.page_link("tomes/tome4/page_75.py", label="75", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
