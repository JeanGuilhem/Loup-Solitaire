import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=236, book=2)

fr_text = """
La panique s'empare du navire. Saisis d'une véritable frénésie, les
marins rassemblent tous les seaux et les couvertures qu'ils peuvent
trouver pour combattre l'incendie. Les flammes jaillissent de l'écoutille
et il faut plus d'une heure pour maîtriser le feu. Les dégâts sont
considérables. Les vivres et les provisions d'eau douce ont été anéantis
et la structure centrale du navire gravement endommagée. Le capitaine
émerge alors de la cale enfumée et s'approche de vous, le visage noir de
suie. Il porte un paquet sous son bras. «Je dois vous parler en privé, my
Lord », dit-il à voix basse. Sans rien répondre, vous le suivez aussitôt
dans sa cabine.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome2/page_222.py", label="222", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
