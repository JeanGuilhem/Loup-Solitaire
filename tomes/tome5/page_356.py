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

check_inventory(current_page_number=356, book=5)

fr_text = """
« J'ai bien connu Tipasa par le passé. A cette époque, j'étais
encore jeune et vigoureux, comme vous... Nous avons combattu
ensemble les pirates Lakuri à Samiz et navigué jusqu'à un
lointain pays où la couche de neige et de glace est si épaisse que
le soleil n'est jamais parvenu à la faire fondre ! Oui, j'ai connu
Tipasa le Vagabond.... mais c'était il y a bien longtemps. Tout ce
que je sais de lui maintenant, c'est qu'il habite à Ikaresh. Mais
allez donc voir la veuve Soushilla : elle est au courant de tout ce
qui se passe dans cette ville. »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_281.py", label="281", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
