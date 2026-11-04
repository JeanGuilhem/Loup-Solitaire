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

check_inventory(current_page_number=268, book=5)

fr_text = """
Tel un tigre, vous vous élancez et vous saisissez la pierre
étincelante une fraction de seconde avant que le poing clouté de
Haakon ne frappe le sol à l'endroit où se trouve le bijou. Vous
vous retournez pour faire face à votre ennemi, la gemme brandie
dans votre main, son rayon bleu brillant jaillissant vers l'armure
noire du Seigneur des Ténèbres. Celui-ci se plie en deux, sous
l'effet du rayon, puis il tombe à genoux alors qu'un horrible bruit
d'aspiration s'élève de son heaume. Peu à peu, Haakon se
recroqueville et disparaît à vos yeux. Un craquement soudain
vous met en alerte, mais vous n'êtes plus en danger : la gemme
éclatante a disparu de votre main ; comme son maître, elle a
quitté cette dimension pour ne plus jamais y revenir.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("A présent, rendez-vous au :"))
    st.page_link("tomes/tome5/page_400.py", label="400", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
