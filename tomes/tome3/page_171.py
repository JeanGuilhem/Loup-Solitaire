import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=171, book=3)

fr_text = """
Le bouchon est coincé dans la fiole et il vous faut l'ôter avec
précaution pour ne pas prendre le risque de briser le verre. Peu à
peu, le bouchon glisse et vous parvenez enfin à l'enlever ; vous
reniflez alors le liquide orange.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous possédez la Discipline Kaï du Sixième Sens ou celle de la Maîtrise des Armes, rendez-vous au :'))
    if has_kai("Le Sixième Sens") or has_kai("La Maîtrise des armes"):
        st.page_link("tomes/tome3/page_311.py", label="311", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome3/page_311.py", label="311", icon="📄", disabled=True)
    st.write_stream(stream_text('Si vous ne maîtrisez aucune de ces deux Disciplines, cette potion ne vous inspire guère confiance et vous décidez de vous en débarrasser. Retournez alors au 10 et faites un nouveau choix :'))
    st.page_link("tomes/tome3/page_10.py", label="10", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
