import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    is_new_page,
    show_illustrations,
    show_map,
)
from text import fr_unknown_magnakai
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=265, book=7)

fr_text = """
Vous plongez votre arme dans l'œil monstrueux, et une
substance fluorescente et gélatineuse s'écoule de la blessure. Un
affreux cri de douleur s'élève alors du sol sous vos pieds, et des
jets de vapeur jaillissent en sifflant à travers le sable. Vous
reculez en essayant de protéger vos yeux du cinglant nuage de
sable qui tourbillonne autour de vous, mais un coup inattendu
dans les jambes vous fait perdre l'équilibre et vous tombez de
tout votre long sur le sol (vous perdez 2 points d'ENDURANCE).
Avant que vous puissiez vous relever, un tentacule vert, recouvert
de verrues, s'enroule lentement autour de votre taille et vous tire
lentement vers l'œil mutilé.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-2)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï du Foudroiement Psychique et si vous souhaitez l'utiliser, rendez-vous au :"))
    if has_magnakai("Foudroiement Psychique"):
        st.page_link("tomes/tome7/page_190.py", label="190", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome7/page_190.py", label="190", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous ne maîtrisez pas cette discipline ou si vous ne voulez pas l'utiliser, rendez-vous au :"))
    st.page_link("tomes/tome7/page_121.py", label="121", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
