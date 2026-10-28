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

check_inventory(current_page_number=227, book=3)

fr_text = """
Les boutons de pierre dépassent d'environ 2 centimètres de la
surface lisse de l'autel. Vous remarquez que d'étranges
hiéroglyphes sont tracés tout autour, mais le temps les a presque
effacés et il est difficile de les distinguer clairement. Il vous faut à
présent décider dans quel ordre vous allez appuyer sur les
boutons. Si vous possédez la Discipline Kaï de la Maîtrise
Psychique de la Matière, vous pourrez les enfoncer sans avoir
besoin de les toucher.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous décidez d'appuyer sur le bouton de gauche, puis sur celui de droite, rendez-vous au :"))
    st.page_link("tomes/tome3/page_102.py", label="102", icon="📄")
    st.write_stream(
        stream_text(
            "Si vous préférez appuyer d'abord sur le bouton de droite et ensuite sur celui de gauche, rendez- "
            "vous au :"
        )
    )
    st.page_link("tomes/tome3/page_334.py", label="334", icon="📄")
    st.write_stream(stream_text("Enfin, si vous décidez d'appuyer sur les deux boutons en même temps, rendez-vous au :"))
    st.page_link("tomes/tome3/page_299.py", label="299", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
