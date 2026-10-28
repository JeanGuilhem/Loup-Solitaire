import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=114, book=3)

fr_text = """
Après avoir parcouru une cinquantaine de mètres environ, vous
arrivez dans une autre caverne. Un Bakanal, féroce créature
Carnivore des terres de Kalte, est étendu sur un gros bloc de
glace, au beau milieu de cet espace glacial. Il semble
profondément endormi, sans doute après avoir fait un copieux
repas à en juger par les ossements répandus autour de lui. Un
autre tunnel s'ouvre dans le mur du fond.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez passer sans bruit devant le Bakanal pour pouvoir emprunter le tunnel, rendez-vous au :"))
    st.page_link("tomes/tome3/page_23.py", label="23", icon="📄")
    st.write_stream(stream_text("Si vous préférez attaquer la créature, rendez-vous au :"))
    st.page_link("tomes/tome3/page_101.py", label="101", icon="📄")
    st.write_stream(stream_text("Enfin, si vous maîtrisez la Discipline Kaï de la Chasse, rendez-vous au :"))
    if has_kai("La Chasse"):
        st.page_link("tomes/tome3/page_279.py", label="279", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome3/page_279.py", label="279", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
