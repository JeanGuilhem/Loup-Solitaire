import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=199, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Vous neutralisez le Garde par une clé à la tête et vous menacez de
lui rompre le cou s'il ne répond pas à vos questions. Il vous
promet immédiatement de vous révéler tout ce qu'il sait. « Le
Zakhan a peur que vous ne soyez un assassin, envoyé par ses
ennemis de l'ouest pour le tuer, dit-il d'une voix apeurée. Moi
aussi je déteste le Zakhan, mais je ne suis qu'un simple geôlier et
je ne sais rien de plus. »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous maîtrisez la Discipline Kaï du Sixième Sens, rendez-vous au :'))
    if has_kai("Le Sixième Sens"):
        st.page_link("tomes/tome5/page_39.py", label="39", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_39.py", label="39", icon="📄", disabled=True)

    st.write_stream(stream_text('Dans le cas contraire, rendez-vous au :'))
    if not has_kai("Le Sixième Sens"):
        st.page_link("tomes/tome5/page_9.py", label="9", icon="📄")
    else:
        st.page_link("tomes/tome5/page_9.py", label="9", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
