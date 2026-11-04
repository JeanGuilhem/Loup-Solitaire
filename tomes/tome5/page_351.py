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

check_inventory(current_page_number=351, book=5)

fr_text = """
Alors que vous vous approchez de la porte, Banedon vous donne
un bon conseil : « Prends garde à ton or, Loup Solitaire ! Rien ne
tente plus les Ikareshis qu'une bourse bien remplie. Tu peux
avoir confiance en leur sens de l'honneur, mais si tu les crois
honnêtes, ils te laisseront nu comme un ver ! » A l'intérieur de
l'auberge règne une atmosphère de fête. Les tables ont été
rapprochées pour former un grand demi-cercle devant lequel se
trouve un homme large d'épaules, vêtu d'un somptueux costume
brodé. Il porte au côté une épée incrustée d'or dans un fourreau
de velours bleu vif, aussi éclatant que son pantalon de soie.
L'homme enlace affectueusement ses compagnons, embrassant
ses amis et les membres de sa famille qui ont parcouru de
nombreux kilomètres pour assister à son mariage. Sa femme est
assise à ses côtés, le visage dissimulé derrière un voile de perles
étincelantes. Soudain, la musique emplit l'auberge et les invités
se pressent au centre de la salle pour entamer la danse du
mariage. A l'autre bout de la pièce, vous apercevez la propriétaire
de l'auberge, une vieille femme corpulente habillée en noir. Les
larmes aux yeux, elle regarde se dérouler les festivités.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez l'approcher pour lui demander où se trouve Tipasa le Vagabond, rendez-vous au :"))
    st.page_link("tomes/tome5/page_276.py", label="276", icon="📄")
    st.write_stream(stream_text("Si vous préférez quitter la taverne et continuer votre chemin, rendez-vous au :"))
    st.page_link("tomes/tome5/page_202.py", label="202", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
