import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=101, book=2)

fr_text = """
Vous vous précipitez à l'intérieur de la cabine du capitaine ; celui-ci
lève les yeux de la carte qu'il était en train d'étudier et vous regarde
d'un air surpris. « Le feu a pris dans la cale ! » Vous avez parlé d'une
voix haletante, le souffle coupé d'avoir tant couru. Un instant plus tard,
le capitaine est sorti de sa cabine et donne l'ordre à ses hommes de
remplir des seaux d'eau et de rassembler des couvertures pour étouffer
l'incendie. Lorsque vous atteignez la cale avant, la fumée s'est épaissie
et, soudain, une véritable frénésie s'empare du navire : des flammes en
effet viennent de jaillir du panneau d'écoutille. Il faut plus d'une heure
pour maîtriser le feu et les dégâts sont considérables. Les vivres et les
réserves d'eau douce étaient entreposés dans cette cale : il n'en reste
plus rien ; de plus, la coque du navire a été endommagée. Le capitaine
remonte de la cale enfumée et s'approche de vous, le visage noir de
suie. Il porte un paquet sous son bras. «Je dois vous parler en privé, my
lord», dit-il à voix basse. Sans dire un mot, vous le suivez jusqu'à sa
cabine.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_222.py", label="222", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
