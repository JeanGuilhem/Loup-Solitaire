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

check_inventory(current_page_number=116, book=7)

fr_text = """
Vous voyez, soudain, avec effroi, la main bondir en l'air, puis
planer au-dessus de votre tête. Tout à coup, ses doigts s'ouvrent
en frémissant et elle se laisse tomber sur vous !
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous maîtrisez la Discipline Magnakaï de l'Art de la Chasse, ajoutez 3 au chiffre que vous avez tiré."))
    roll = hazard_roll(key="main")
    if roll is not None:
        total = roll + (3 if has_magnakai("Art de la Chasse") else 0)
        if has_magnakai("Art de la Chasse"):
            st.write(f"*Art de la Chasse : +3, total {total}.*")
        if total <= 2:
            st.write_stream(stream_text("Si le résultat est compris entre 0 et 2, rendez-vous au :"))
            st.page_link("tomes/tome7/page_77.py", label="77", icon="📄")
        elif total <= 6:
            st.write_stream(stream_text("Si le résultat est compris entre 3 et 6, rendez-vous au :"))
            st.page_link("tomes/tome7/page_198.py", label="198", icon="📄")
        else:
            st.write_stream(stream_text("Si le résultat est supérieur ou égal à 7, rendez-vous au :"))
            st.page_link("tomes/tome7/page_235.py", label="235", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
