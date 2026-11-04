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

check_inventory(current_page_number=317, book=5)

fr_text = """
Votre cœur bat à tout rompre tandis que vous gravissez les
marches de marbre. A une vingtaine de mètres devant vous, il y a
un palier où se trouve une porte en pierre. Au-delà, l'escalier
continue à monter vers un chemin de ronde muni d'un parapet
au bout duquel se trouve une autre porte en pierre, identique à la
première. Soudain, la porte du palier s'ouvre à la volée et un
Garde surgit dans l'encadrement, face à vous. « Par le Majhan ! »
s'écrie-t-il en portant la main à son épée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous désirez attaquer le Garde avant qu'il ne dégaine son arme, rendez-vous au :"))
    st.page_link("tomes/tome5/page_338.py", label="338", icon="📄")

    st.write_stream(stream_text("Si vous préférez le bousculer et continuer à monter l'escalier en courant, rendez-vous au :"))
    st.page_link("tomes/tome5/page_372.py", label="372", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
