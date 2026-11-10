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

check_inventory(current_page_number=203, book=7)

fr_text = """
Les mains tremblantes, vous serrez la corde verte le plus fort
possible tout en essayant de bloquer vos pieds pour ne pas glisser
dans les énormes vagues qui rugissent en dessous. La coque en
bois craque dans la nuit, puis le bateau est rapidement englouti
sans laisser de trace. Soudain, une brusque secousse parcourt
toute la longueur de la corde, et une espèce de tête de serpent
surgit des eaux noires. Elle se dresse en ondulant, et les
mâchoires grandes ouvertes laissent voir de longs crochets
jaunes aiguisés comme des couteaux. L'ignoble tête vous fixe de
ses yeux blancs et aveugles, prête à attaquer. Vous comprenez
alors avec effroi que vous vous cramponnez, en réalité, au corps
d'un redoutable Lekhor !
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez lâcher le corps du serpent et plonger dans les eaux noires, rendez-vous au :"))
    st.page_link("tomes/tome7/page_325.py", label="325", icon="📄")

    st.write_stream(stream_text("Si vous préférez tirer une arme pour vous défendre contre son attaque venimeuse, rendez-vous au :"))
    st.page_link("tomes/tome7/page_76.py", label="76", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
