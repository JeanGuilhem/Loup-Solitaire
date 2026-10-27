import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=49, book=2)

fr_text = """
Pendant trois jours et trois nuits, les navires de la flotte de Durenor font
voile en direction du golfe de Holm. La traversée est rapide mais
chacun des bateaux est malheureusement frappé par la malchance. Des
voiles se déchirent, des cordages se dénouent mystérieusement et des
voies d'eau se forment dans les coques. Les hommes entassés à bord se
laissent gagner par l'énervement, des querelles éclatent, puis des
bagarres, qui souvent se terminent par la mort d'un des adversaires. Au
bout de la troisième nuit, Lord Axim est au bord du désespoir. «Je n'ai
jamais subi une aussi mauvaise traversée, dit-il, nous n'avons croisé
aucun ennemi, nous n'avons livré aucune bataille et pourtant, la moitié
de mes hommes sont malades ou blessés et nous avons perdu deux de
nos plus beaux navires. La lune nous est contraire, une malédiction
pèse sur nous. Puisse-t-elle se dissiper bientôt car, même si nous
arrivions à Holmgard cette nuit même, nous n'aurions pas la force de
repousser l'ennemi qui assiège la ville. » Tandis qu'il prononce ces
paroles, vous voyez l'aube se lever. Vous pensez que ce jour nouveau
vous apportera peut-être quelque soulagement mais, hélas, les eaux
calmes qui vous entourent sont trompeuses et cachent en fait une
menace mortelle.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome2/page_100.py", label="100", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
