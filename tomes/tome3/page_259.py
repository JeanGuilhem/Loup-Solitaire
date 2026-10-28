import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=259, book=3)

fr_text = """
Soudain, Fenor se relève d'un bond et saisit son épée. « C'est un
Languabarb ! s'écrie-t-il. Vite ! prenez vos armes ou nous
sommes perdus. » Les autres se hâtent d'empoigner leurs armes
tandis que Fenor disparaît au-dehors. Presque immédiatement,
un hurlement de douleur retentit et quelque chose se trouve
violemment projeté contre la toile de la tente qui s'écroule
aussitôt sous le choc. Vous vous retrouvez alors couché côte à
côte avec le cadavre mutilé de Fenor. Saisi de panique, vous vous
dépêtrez de la toile de tente et vous tirez votre arme. A ce
moment, un énorme monstre quadrupède vous saute dessus. Ses
yeux rouges brillent comme deux charbons ardents et sa gueule
ouverte, hérissée de dents pointues, laisse apparaître une langue
couverte d'un poil rêche. La bête est sur vous et il vous faut la combattre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("LANGUABARB", 11, 35)], stop_when_wounded=True)
    if outcome == "wounded":
        st.write_stream(stream_text("Vous avez perdu des points d'ENDURANCE au cours de ce combat. Rendez-vous immédiatement au :"))
        st.page_link("tomes/tome3/page_129.py", label="129", icon="📄")
    elif outcome == "win":
        st.write_stream(stream_text("Vous avez tué la créature sans perdre un seul point d'ENDURANCE. Rendez-vous au :"))
        st.page_link("tomes/tome3/page_151.py", label="151", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
