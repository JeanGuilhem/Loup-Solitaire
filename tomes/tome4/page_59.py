import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=59, book=4)

fr_text = """
Le capitaine Gayal et ses hommes sont engagés dans un combat
sans merci contre l'ennemi à cheval. Ils sont surpassés en
nombre par des adversaires impitoyables dont les chevaux sont
équipés de fers hérissés de pointes. Leur technique consiste à
projeter leurs victimes à terre puis à les faire piétiner par leurs
montures. Lorsque vous atteignez la barricade, une autre vague
d'attaquants s'approche. Des maîtres chiens vêtus d'armures se
déploient devant une troupe d'infanterie armée de lances. Ils
tiennent en laisse des meutes de Chiens de Guerre. A une
cinquantaine de mètres de la barricade, les hommes en armure
s'immobilisent et se penchent pour lâcher leurs molosses.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    number = hazard_roll()
    if number is not None and number <= 4:
        st.write_stream(stream_text("Si vous tirez un chiffre de 0 à 4, rendez-vous au :"))
        st.page_link("tomes/tome4/page_193.py", label="193", icon="📄")
    elif number is not None:
        st.write_stream(stream_text("De 5 à 9, rendez-vous au :"))
        st.page_link("tomes/tome4/page_260.py", label="260", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
