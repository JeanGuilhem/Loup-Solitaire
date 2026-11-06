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

check_inventory(current_page_number=159, book=6)

fr_text = """
« Vous nous insultez, étranger ! » siffle l'homme à la balafre en
sautant sur ses pieds. Subitement, un silence de mort tombe sur
la grande salle et tous les regards sont fixés sur vous. A la table
de gauche, quelques marchands se lèvent et s'éloignent
précipitamment, tandis que les deux autres guerriers dégainent
leur épée après avoir violemment renversé la table. « A l'attaque !
» s'écrient-ils à l'unisson en joignant le geste à la parole.
Combattez les trois hommes comme s'ils ne faisaient qu'un. Vous
ne pouvez ni fuir ni vous servir de votre Arc durant la lutte.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # trois hommes combattus comme un seul ; ni fuite ni Arc
    outcome = combat([("MERCENAIRES DE VARETTA", 26, 35)])
    if outcome == "win":
        st.write_stream(stream_text("Si vous sortez vainqueur du combat, rendez-vous au :"))
        st.page_link("tomes/tome6/page_48.py", label="48", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
