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

check_inventory(current_page_number=255, book=6)

fr_text = """
Lorsque les mots du chef parviennent à vos oreilles, une douleur
lancinante commence à vous vriller les tempes. Vous comprenez
alors que vous êtes attaqué par une puissante Force Psychique et
que vous devez utiliser votre Écran Psychique pour arrêter
efficacement cet Assaut. Mais, habilement, vous faites semblant de
vous tordre de douleur pour faire croire au chef qu'il a remporté
la victoire. Tout le monde dans la procession semble se réjouir à
la vue de vos souffrances feintes, comme si vos cris de douleur
étaient de la musique à leurs oreilles. Ils se précipitent alors
sur vous en tirant des poignards cachés sous leurs robes de bure
et tentent de vous encercler.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez éviter cet Assaut, rendez-vous au :"))
    st.page_link("tomes/tome6/page_289.py", label="289", icon="📄")

    st.write_stream(stream_text("Si vous préférez engager le combat avec ces hommes malfaisants, rendez-vous au :"))
    st.page_link("tomes/tome6/page_194.py", label="194", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
