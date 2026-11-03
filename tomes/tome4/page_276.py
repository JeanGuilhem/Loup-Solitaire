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

check_inventory(current_page_number=276, book=4)

fr_text = """
Un grognement terrifiant retentit bientôt. Vos hommes et vous-
même vous immobilisez en voyant le mur du fond s'avancer
soudain vers vous. Une crevasse apparaît qui s'élargit en révélant
deux rangées de dents tranchantes comme des rasoirs. Vous avez
réveillé un Ver de Pierre affamé qui a l'intention de vous inscrire
au menu de son prochain repas. Vos patrouilleurs dégainent
leurs épées et se préparent au combat. Il est trop tard pour qu'ils
puissent prendre la fuite.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez combattre le Ver de Pierre, rendez-vous au :'))
    st.page_link("tomes/tome4/page_88.py", label="88", icon="📄")
    st.write_stream(stream_text("Contrairement à vos hommes qui se trouvent devant, vous pouvez peut-être essayer de fuir en retournant vers l'échelle. Rendez-vous pour cela au :"))
    st.page_link("tomes/tome4/page_26.py", label="26", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
