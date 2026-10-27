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

check_inventory(current_page_number=204, book=2)

fr_text = """
L'exceptionnelle acuité visuelle que vous avez acquise au cours de
votre entraînement à la Discipline de l'Orientation vous permet de
distinguer nettement le talisman fixé à l'extrémité du bâton noir. C'est
l'emblème de la Guilde des Magiciens de Toran : un croissant et une
étoile de cristal. Cet homme est un renégat qui a trahi tout à la fois la
Guilde et votre patrie.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez monter en haut de cette tour pour attaquer le magicien félon, rendez-vous au :'))
    st.page_link("tomes/tome2/page_73.py", label="73", icon="📄")

    st.write_stream(stream_text('Si vous ne voulez pas risquer votre vie en affrontant ce puissant sorcier, sautez par-dessus bord et rendez-vous au :'))
    st.page_link("tomes/tome2/page_267.py", label="267", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
