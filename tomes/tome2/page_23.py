import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=23, book=2)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Pendant près de dix minutes, vous poursuivez la créature qui s'enfuit le
long d'un passage étroit et sinueux. Vous êtes sur le point d'abandonner
lorsque le passage s'ouvre soudain sur une immense caverne éclairée
par des torches enflammées. Un spectacle saisissant s'offre alors à vous.
L'endroit, en effet, abrite une colonie entière de ces étranges créatures,
les Noudics, qui sont fort occupées à examiner et à trier toutes sortes
d'objets insolites empilés les uns sur les autres au beau milieu de la
caverne.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï de la Communication Animale, rendez-vous au :"))
    if has_kai("Communication Animale"):
        st.page_link("tomes/tome2/page_144.py", label="144", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome2/page_144.py", label="144", icon="📄", disabled=True)
    st.write_stream(stream_text("Dans le cas contraire, rendez-vous au :"))
    st.page_link("tomes/tome2/page_295.py", label="295", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
