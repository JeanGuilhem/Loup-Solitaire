import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=58, book=3)

fr_text = """
Le cône de givre s'enfonce dans le feuillage des plantes et les gèle
instantanément. Tiges et feuilles deviennent alors cassantes et se
brisent sous votre poids. Sans un instant d'hésitation, vous vous
précipitez vers l'extrémité du pont végétal et vous parvenez à
bondir sur la plate-forme où se tient Vonotar juste avant que les
plantes ne se soient complètement désagrégées. Vous avez réussi
à traverser le fossé, mais à présent, vous êtes étendu aux pieds de
Vonotar qui se met à ricaner en pointant sa baguette de cristal
sur votre tête.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome3/page_252.py", label="252", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
