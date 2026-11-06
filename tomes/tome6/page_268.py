import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import bow_shot, called_cookies, stream_text

# fait testé : "Arc en Chêne" (page 252) : +3 au tir, en plus de la Science des Armes

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=268, book=6)

fr_text = """
Vous tendez la corde de votre Arc et visez les yeux brillants de
la créature.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous maîtrisez la Discipline Magnakaï de la Science des Armes pour l'Arc, ajoutez 3 au chiffre que vous avez obtenu."))
    total = bow_shot(key="t6_268")  # bonus de l'Arc en Chêne compris
    if total is not None:
        if total <= 5:
            st.write_stream(stream_text("Si votre total est compris entre 0 et 5, rendez-vous au :"))
            st.page_link("tomes/tome6/page_155.py", label="155", icon="📄")
        elif total <= 8:
            st.write_stream(stream_text("Si votre total est compris entre 6 et 8, rendez-vous au :"))
            st.page_link("tomes/tome6/page_236.py", label="236", icon="📄")
        else:
            st.write_stream(stream_text("Si votre total est compris entre 9 et 12, rendez-vous au :"))
            st.page_link("tomes/tome6/page_75.py", label="75", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
