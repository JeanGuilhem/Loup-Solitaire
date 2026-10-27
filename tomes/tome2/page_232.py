import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    has_kai,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=232, book=2)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."
fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
Vous êtes parvenu à moins d'une vingtaine de mètres de la tour lorsque
le garde fait un pas en avant et vous demande ce que vous venez faire
par ici. Vous remarquez que le soldat porte la vareuse rouge de
l'uniforme des armées durenoraises, ce qui signifie que vous avez
atteint la frontière du royaume. Il vous faut à présent trouver le moyen
de passer.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez prétendre que vous êtes un marchand en route pour Port Bax, rendez-vous au :'))
    st.page_link("tomes/tome2/page_250.py", label="250", icon="📄")

    st.write_stream(stream_text("Si vous voulez essayer de le corrompre en lui donnant de l'or, rendez-vous au :"))
    st.page_link("tomes/tome2/page_68.py", label="68", icon="📄")

    st.write_stream(stream_text("Si vous pensez qu'il est préférable de lui montrer le Sceau d'Hammardal (en admettant qu'il soit toujours en votre possession), rendez-vous au :"))
    if has_item("SCEAU D'HAMMARDAL"):
        st.page_link("tomes/tome2/page_223.py", label="223", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome2/page_223.py", label="223", icon="📄", disabled=True)

    st.write_stream(stream_text('Enfin, si vous maîtrisez la Discipline Kaï du Sixième Sens, rendez-vous au :'))
    if has_kai('Le Sixième Sens'):
        st.page_link("tomes/tome2/page_149.py", label="149", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome2/page_149.py", label="149", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
