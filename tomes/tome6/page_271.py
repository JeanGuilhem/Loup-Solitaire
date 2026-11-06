import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=271, book=6)

fr_text = """
Vous avez à peine parcouru une centaine de mètres lorsque vous
entendez derrière vous quelqu'un hurler : «Au voleur! Au voleur!
Il a volé mon cheval! Attrapez-le ! » Vous vous raidissez sur
votre selle et vous éperonnez les flancs de votre monture. Vous
descendez au galop la route sinueuse et longez la haie qui borde
la lice. Les cris ont alerté quelques hommes en train de disputer
un tournoi de tir à l'arc. Ils se précipitent aussitôt hors du
champ et se mettent en travers de la route. Dès qu'ils vous
aperçoivent, ils tendent les cordes de leurs arcs et vous tirent
dessus.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous maîtrisez la Discipline Magnakaï du Contrôle Animal ou de l'Art de la Chasse, ajoutez 3 au chiffre obtenu."))
    roll = hazard_roll(key="t6_271")
    if roll is not None:
        bonus = 3 if has_magnakai("Contrôle Animal") or has_magnakai("Art de la Chasse") else 0
        total = roll + bonus
        if bonus:
            st.write(f"*Discipline Magnakaï : +3, soit un total de {total}.*")
        if total <= 5:
            st.write_stream(stream_text("Si votre total est inférieur ou égal à 5, rendez-vous au :"))
            st.page_link("tomes/tome6/page_52.py", label="52", icon="📄")
        else:
            st.write_stream(stream_text("Si votre total est égal ou supérieur à 6, rendez-vous au :"))
            st.page_link("tomes/tome6/page_81.py", label="81", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
