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

check_inventory(current_page_number=311, book=4)

fr_text = """
Trois soldats du Sommerlund se précipitent pour vous venir en
aide. Abattant leurs épées sur les Chiens de Guerre, ils
parviennent à tuer en quelques instants les monstrueuses
créatures. Vous vous relevez tant bien que mal en essayant de
faire le point de la situation, tandis que la bataille fait rage autour
de vous. Les soldats du Sommerlund contrôlent toujours la
barricade, se rassemblant en groupes devant les brèches pour
empêcher l'ennemi de s'infiltrer. Des lances et des flèches volent
en tous sens, s'enfonçant dans le métal, le bois, et dans la chair
des combattants. Des hommes tombent de leurs chevaux : leurs
montures hennissent et s'emballent ; le sol est jonché de
cadavres et de soldats blessés. Les Chiens de Guerre ont été
repoussés vers leurs maîtres armés de lances qui s'approchent à
présent derrière un mur de boucliers. A votre droite, un brigand
essaie de sauter la barricade à cheval. Mais l'animal est blessé et
à l'agonie : il lui est impossible de bondir. Son cavalier est projeté
en avant et tombe derrière vous.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez attaquer ce Guerrier Pillard, rendez-vous au :"))
    st.page_link("tomes/tome4/page_90.py", label="90", icon="📄")

    st.write_stream(stream_text("Si vous préférez rassembler les soldats du Sommerlund pour repousser l'avance des lanciers, rendez-vous au :"))
    st.page_link("tomes/tome4/page_3.py", label="3", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
