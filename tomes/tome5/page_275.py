import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=275, book=5)

fr_text = """
Vous reconnaissez le drapeau qui flotte au-dessus d'une plate-forme
fortifiée, située au centre de cet étrange vaisseau. Il s'agit
de la bannière de la guilde des Magiciens de Toran, une ville du
nord du Sommerlund, portant comme emblème un croissant et
une étoile de cristal. Le vaisseau de l'espace est commandé par
un magicien Sommerlundois, un de vos compatriotes. Il a de
longs cheveux blonds et est vêtu d'un habit bleu foncé. Vous êtes
tellement frappé par cette extraordinaire apparition, que vous ne
voyez même pas le sang qui coule de la bouche de votre Itikar. En
effet, la créature est toute proche de la mort et pousse soudain un
long croassement qui vous fend le cœur. Puis ses ailes se
raidissent et sa tête tombe mollement en avant tandis que le
dernier souffle de vie s'échappe de son corps meurtri. Vous êtes
violemment projeté à bas de la selle et vous tombez comme une
pierre, l'estomac noué, vers le lac Inrahim.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    roll = hazard_roll()
    if roll is not None and roll <= 4:
        st.write_stream(stream_text("Si vous avez tiré un chiffre entre 0 et 4, rendez-vous au :"))
        st.page_link("tomes/tome5/page_374.py", label="374", icon="📄")
    elif roll is not None and roll <= 8:
        st.write_stream(stream_text("Si vous avez tiré un chiffre entre 5 et 8, rendez-vous au :"))
        st.page_link("tomes/tome5/page_254.py", label="254", icon="📄")
    elif roll is not None:
        st.write_stream(stream_text("Si vous avez tiré un 9, rendez-vous au :"))
        st.page_link("tomes/tome5/page_261.py", label="261", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
