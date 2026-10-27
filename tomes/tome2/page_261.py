import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=261, book=2)

fr_text = """
Sur un bon nombre de kilomètres, la route longe une hauteur
verdoyante, où abonde l'herbe grasse, avant de tourner enfin vers le
nord, en direction de la côte. Vous arrivez dans un village dont les
maisons sont bâties en cercle autour d'un étang et lorsque vous le
traversez, un groupe d'enfants squalls se précipite vers vous en hurlant
et en vous lançant des pierres. Vous descendez ensuite dans la profonde
vallée qui s'étend au-delà et, peu à peu, la lande laisse place à des terres
plus riches qui ont été défrichées et cultivées. La colline qui se dresse
de l'autre côté est couverte de forêts ; vous n'êtes plus loin de la côte à
présent, et vous apercevez déjà ses hautes falaises et la couleur des rocs
qui surplombent la mer. Un peu plus tard, vous êtes en train de franchir
un taillis lorsque des appels à l'aide retentissent à votre droite.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez vous porter au secours de la personne qui crie ainsi, rendez-vous au :'))
    st.page_link("tomes/tome2/page_95.py", label="95", icon="📄")

    st.write_stream(stream_text('Si vous préférez ne pas prêter attention à ces hurlements désespérés, continuez de chevaucher le long de la route en vous rendant au :'))
    st.page_link("tomes/tome2/page_198.py", label="198", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
