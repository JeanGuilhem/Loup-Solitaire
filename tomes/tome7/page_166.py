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

check_inventory(current_page_number=166, book=7)

fr_text = """
Au bout de quelques pas, le silence est rompu par un autre
claquement. Le fouet invisible vous mord les mollets, et vos
genoux fléchissent ; vous tressaillez sous la douleur et perdez
l'équilibre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous maîtrisez la Discipline Magnakaï de l'Art de la Chasse, ajoutez 2 au chiffre que vous avez tiré."))
    roll = hazard_roll(key="fouet")
    if roll is not None:
        total = roll + (2 if has_magnakai("Art de la Chasse") else 0)
        if total != roll:
            st.write(f"*Art de la Chasse : +2, soit un total de {total}.*")
        st.write_stream(stream_text("Si le résultat est compris entre 0 et 2, rendez-vous au :"))
        st.page_link("tomes/tome7/page_275.py", label="275", icon="📄", disabled=total > 2)
        st.write_stream(stream_text("Si le résultat est compris entre 3 et 7, rendez-vous au :"))
        st.page_link("tomes/tome7/page_222.py", label="222", icon="📄", disabled=not 3 <= total <= 7)
        st.write_stream(stream_text("Si le résultat est supérieur ou égal à 8, rendez-vous au :"))
        st.page_link("tomes/tome7/page_311.py", label="311", icon="📄", disabled=total < 8)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
