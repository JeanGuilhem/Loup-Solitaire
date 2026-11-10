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

check_inventory(current_page_number=202, book=7)

fr_text = """
Des flammes bleues fusent de la baguette de Zahda.
Instinctivement, vous vous jetez au sol pour éviter d'être brûlé. Il
était temps: la décharge vous frôle avant d'exploser dans une
gerbe d'étincelles multicolores. Poussant un cri de colère et de
dépit, Zahda bondit alors sur vous. Roulant sur le côté, vous
l'esquivez au moment même où il allait vous fracasser le crâne.
Vous l'avez échappé belle : le coup était si violent qu'il en a fendu
le sol ! Une flamme jaillit de la fissure et brûle la main du
seigneur en furie. Celui-ci se met à crier comme un corbeau
blessé et laisse tomber sa baguette de ses mains noircies par le
feu. Vous en profitez pour attaquer, mais Zahda réagit
promptement : il se redresse et se tient maintenant fermement
au bord de l'abîme en brandissant un poignard à la lame
étincelante. Le Seigneur Zahda est immunisé contre la Puissance
Psychique mais pas contre le Foudroiement Psychique.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("ZAHDA", 25, 45)], psychic_power_immune=True)
    if outcome == "win":
        st.write_stream(stream_text("Si vous remportez le combat, rendez-vous au :"))
        st.page_link("tomes/tome7/page_149.py", label="149", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
