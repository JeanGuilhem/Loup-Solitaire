import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies, handle_repas

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=150, book=2)

fr_text = """
Vous lancez votre cheval dans les rues sinueuses du village, puis vous
traversez un pont de bois ; vous montez ensuite un sentier escarpé qui
conduit au sommet d'une crique. A la clarté de la lune, vous apercevez
un poteau indicateur orienté vers l'est. Vous chevauchez toute la nuit
sans prendre le temps de dormir et lorsque l'aube se lève enfin, le
paysage s'est métamorphosé d'une manière surprenante. Les terres
arides du Pays Sauvage ont fait place à des landes et à des marécages,
et, aussi loin que porte le regard, une ombre noire s'étend à l'horizon en
direction de l'est. C'est la forêt de Durenor, la frontière naturelle du
royaume des montagnes qui borde à cet endroit les espaces inexplorés
du Pays Sauvage. Voilà sans nul doute une vision réconfortante qui
vous met quelque baume au cœur. Vous n'êtes plus qu'à une journée de
cheval de Port Bax, mais vous êtes épuisé après cette nuit blanche et il
vous faut prendre un repas ou vous perdrez 3 points d'ENDURANCE.
Si vous maîtrisez la Discipline Kaï de la Chasse, vous pouvez en faire
usage et capturer du gibier qui vous fournira les viandes nécessaires
pour reprendre des forces. Vous avez chevauché pendant une heure
lorsque vous arrivez à une bifurcation, mais vous ne voyez aucun
poteau indicateur.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    handle_repas()
    st.write_stream(stream_text("Si vous souhaitez prendre le chemin de gauche, rendez-vous au :"))
    st.page_link("tomes/tome2/page_261.py", label="261", icon="📄")
    st.write_stream(stream_text("Si vous préférez aller à droite, rendez-vous au :"))
    st.page_link("tomes/tome2/page_334.py", label="334", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
