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

check_inventory(current_page_number=293, book=7)

fr_text = """
Vous traversez furtivement la grande galerie aux dalles
craquelées, les muscles tendus et les sens aux aguets, à l'écoute
du moindre danger. Le bruit continu de l'eau qui tombe et le
hurlement de la tempête ajoutent encore à l'extrême désolation
de la pièce. Une jungle de ronces envahit les murs, s'enroulant
autour des cadres pourris des tableaux et courant sur les
tapisseries humides et moisies. Une grande épée d'Anarie est
suspendue au-dessus de la cheminée, la pointe tournée sur le
côté. Vous suivez des yeux la lame rouillée et vous remarquez une
forme allongée dans l'âtre. En vous approchant, vous découvrez
qu'il s'agit du corps d'un homme mort. Derrière se trouve un
panneau que le cadavre maintient grand ouvert. Vous regardez à
l'intérieur et apercevez des marches qui descendent dans
l'obscurité.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez fouiller le corps, rendez-vous au :"))
    st.page_link("tomes/tome7/page_146.py", label="146", icon="📄")

    st.write_stream(stream_text("Si vous voulez explorer le passage secret, rendez-vous au :"))
    st.page_link("tomes/tome7/page_11.py", label="11", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
