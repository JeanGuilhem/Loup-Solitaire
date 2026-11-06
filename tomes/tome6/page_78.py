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

check_inventory(current_page_number=78, book=6)

fr_text = """
Vous vous préparez au combat et vous vous lancez au secours du
pauvre vieillard impuissant, juste à temps pour parer le coup
que le nobliau s'apprêtait à lui assener à l'aide de son épée. «
Maudit sois-tu, vermine ! s'écrie-t-il. Je suis Roark, seigneur
d'Amory. Comment oses-tu te mêler de mes affaires ? » Sur ces
paroles, l'homme fait mine de se retirer, mais vous n'êtes pas
dupe de cette manœuvre grossière : au moment où il fend l'air de
son épée d'un traître revers du bras, vous êtes déjà prêt à
esquiver son coup ! La taverne retentit de cris et de vivats à
la perspective du combat spectaculaire qui s'annonce.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous réduisez le total d'ENDURANCE de Roark à 11, ou moins, rendez-vous au 180 au lieu de poursuivre la lutte."))
    outcome = combat([("ROARK", 24, 30)], enemy_stop_at=11)
    if outcome == "win":
        st.write_stream(stream_text("Roark n'a plus que 11 points d'ENDURANCE, ou moins : rendez-vous au :"))
        st.page_link("tomes/tome6/page_180.py", label="180", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
