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

check_inventory(current_page_number=222, book=2)

fr_text = """
Après avoir soigneusement refermé la porte de sa cabine, le capitaine
ouvre son mystérieux paquet et en répand le contenu sur une table. 11
s'agit d'une cruche de faïence noircie et de lambeaux d'étoffe calcinés
qui dégagent une étrange odeur d'huile. « Cet incendie n'est pas un
accident, déclare le capitaine Kelman d'une voix solennelle, c'est un
acte de sabotage. Cette cruche d'huile et ces chiffons que j'ai trouvés
sur le plancher de la cale n'avaient rien à y faire ; quelqu'un à bord de
ce navire est prêt à risquer sa vie pour nous empêcher d'atteindre
Durenor. » Vous contemplez tous deux les chiffons brûlés, comme s'ils
pouvaient répondre aux questions que vous vous posez. Et soudain un
cri retentit au-dessus de vos têtes, brisant le silence qui règne dans la
cabine. « Navire en vue ! Navire en vue sur bâbord avant ! » Le
capitaine saisit aussitôt sa lunette d'approche et se hâte de monter sur le
pont par une échelle d'écoutille.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous désirez le suivre, rendez-vous au :'))
    st.page_link("tomes/tome2/page_175.py", label="175", icon="📄")

    st.write_stream(stream_text('Si vous préférez fouiller rapidement sa cabine, rendez-vous au :'))
    st.page_link("tomes/tome2/page_315.py", label="315", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
